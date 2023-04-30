import configparser
import os

config = configparser.ConfigParser()
config.read('./app/config.ini')

os.environ["SLACK_APP_TOKEN"] = config.get('slack', 'app_token')
os.environ["SLACK_BOT_TOKEN"] = config.get('slack', 'bot_token')