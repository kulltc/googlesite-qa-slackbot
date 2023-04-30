import configparser
import os

config = configparser.ConfigParser()
config.read('./app/config.ini')

os.environ["OPENAI_API_KEY"] = config.get("openai", "api_key")