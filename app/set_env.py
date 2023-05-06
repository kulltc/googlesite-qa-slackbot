import configparser
import os

config = configparser.ConfigParser()
config.read('./app/config.ini')

def set_env():
    os.environ["SLACK_APP_TOKEN"] = config.get('slack', 'app_token')
    os.environ["SLACK_BOT_TOKEN"] = config.get('slack', 'bot_token')
    os.environ["RABBITMQ_HOST"] = config.get('rabbitmq', 'host')
    os.environ["RABBITMQ_QUEUE"] = config.get('rabbitmq', 'queue')
    os.environ["RABBITMQ_USER"] = config.get('rabbitmq', 'user')
    os.environ["RABBITMQ_PASSWORD"] = config.get('rabbitmq', 'password')