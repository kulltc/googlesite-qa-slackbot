
from slackbot.slack_app import SlackBot
from query_ai.langchain_loader import setup_loader_and_index

index = setup_loader_and_index()
slackbot = SlackBot(index.query_with_sources)

if __name__ == "__main__":
    slackbot.start()