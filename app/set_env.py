import configparser
import os
import logging
from pathlib import Path

# get the absolute path of the current script
script_location = Path(os.path.abspath(__file__))

# get the directory containing the script
script_dir = script_location.parent

# construct the full path to the config file
config_file = script_dir / 'config.ini'

# load the config parser
config = configparser.ConfigParser()
config.read(config_file)

def set_env():
    os.environ["SLACK_APP_TOKEN"] = config.get('slack', 'app_token')
    os.environ["SLACK_BOT_TOKEN"] = config.get('slack', 'bot_token')
    os.environ["SLACK_CHANNELS"] = config.get('slack', 'allowed_channels')
    os.environ["RABBITMQ_HOST"] = config.get('rabbitmq', 'host')
    os.environ["RABBITMQ_QUEUE"] = config.get('rabbitmq', 'queue')
    os.environ["RABBITMQ_USER"] = config.get('rabbitmq', 'user')
    os.environ["RABBITMQ_PASSWORD"] = config.get('rabbitmq', 'password')
    os.environ["OPENAI_API_KEY"] = config.get('openai', 'api_key')
    os.environ["OPENAI_MODEL"] = config.get('openai', 'model')
    os.environ['FALLBACK_RESPONSE'] = config.get('DEFAULT', 'fallback_response')
    os.environ['NO_ANSWER_INSTRUCTION'] = config.get('DEFAULT', 'no_answer_instruction')
    os.environ['CHROMADB_COLLECTION_NAME'] = config.get('chromadb', 'collection_name')
    if isinstance(config.get('logging', 'level'), int):
        logging.basicConfig(level=config.get('logging', 'level'))