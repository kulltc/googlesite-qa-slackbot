# rabbitmq_consumer.py
import os
import json
import pika
from set_env import set_env
set_env()

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

from query_ai.langchain_loader import load
from slackbot.response_formatter import format_query_response_with_sources




chain = load()
client = WebClient(token=os.environ["SLACK_BOT_TOKEN"])

def handle_message(channel, method, properties, body):
    event = json.loads(body)

    query = event["text"]
    response = chain(query)
    formatted_response = format_query_response_with_sources(response, os.environ['FALLBACK_RESPONSE'])
    
    try:
        client.chat_postMessage(channel=event["channel"], text=formatted_response)
    except SlackApiError as e:
        print(f"Error sending message: {e}")

    channel.basic_ack(delivery_tag=method.delivery_tag)

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host=os.environ["RABBITMQ_HOST"],
        credentials=pika.PlainCredentials(os.environ["RABBITMQ_USER"], os.environ["RABBITMQ_PASSWORD"])
    ))
    channel = connection.channel()
    channel.queue_declare(queue=os.environ["RABBITMQ_QUEUE"])

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue=os.environ["RABBITMQ_QUEUE"], on_message_callback=handle_message)

    print("Waiting for messages. To exit press CTRL+C")
    channel.start_consuming()

if __name__ == "__main__":
    main()