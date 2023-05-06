# slack_app.py
import os
import json
import pika

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

class SlackBot:
    def __init__(self):
        self.app = App()

        @self.app.event({"type": "message", "subtype": None})
        def handle_messages_event(body, say, logger):
            self.handle_messages(body, say, logger)

    def handle_messages(self, body, say, logger):
        event = body["event"]

        if event.get("subtype") == "bot_message":
            return

        if "app_mention" in event["text"] or event["channel"].startswith("D"):
            connection = pika.BlockingConnection(pika.ConnectionParameters(
                host=os.environ["RABBITMQ_HOST"],
                credentials=pika.PlainCredentials(os.environ["RABBITMQ_USER"], os.environ["RABBITMQ_PASSWORD"])
            ))
            channel = connection.channel()
            channel.queue_declare(queue=os.environ["RABBITMQ_QUEUE"])
            channel.basic_publish(exchange='', routing_key=os.environ["RABBITMQ_QUEUE"], body=json.dumps(event))
            connection.close()

    def start(self):
        handler = SocketModeHandler(self.app, os.environ["SLACK_APP_TOKEN"])
        handler.start()
