from slackbot.slack_app import SlackBot
from set_env import set_env

set_env()

def main():
    slackbot = SlackBot()
    slackbot.start()

if __name__ == "__main__":
    main()
