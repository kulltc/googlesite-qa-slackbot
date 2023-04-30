import os
from slack_bolt import App
from slackbot.response_formatter import format_query_response_with_sources
from slack_bolt.adapter.socket_mode import SocketModeHandler

class SlackBot:
    def __init__(self, query_handler):
        self.app = App()
        self.query_handler = query_handler

        @self.app.event({"type": "message", "subtype": None})
        def handle_messages_event(body, say, logger):
            self.handle_messages(body, say, logger)

    def handle_messages(self, body, say, logger):
        event = body["event"]

        if event.get("subtype") == "bot_message":
            return

        if "app_mention" in event["text"] or event["channel"].startswith("D"):
            query = event["text"]
            response = self.query_handler(query)
            say(format_query_response_with_sources(response))

    def start(self):
        handler = SocketModeHandler(self.app, os.environ["SLACK_APP_TOKEN"])
        handler.start()
