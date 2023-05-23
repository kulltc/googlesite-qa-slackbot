#import argparse
#parser = argparse.ArgumentParser()
#parser.add_argument("query", nargs=1)
#args = parser.parse_args()

import logging
logging.basicConfig(level=50)
from typing import Optional
from .app.slackbot.response_formatter import format_query_response_with_sources
import os
from .app.set_env import set_env
set_env()
from .app.query_ai.langchain_loader import load
from evals.api import CompletionFn, CompletionResult

chain = load()
chain.return_source_documents = True

import evals
import evals.metrics

class SlackBotCompletionResult(CompletionResult):
    def __init__(self, response) -> None:
        self.response = response

    def get_completions(self) -> list[str]:
        print(f'returning: {self.response}')
        return [self.response.strip()]

class SlackbotCompletionFunction(CompletionFn):
    def __init__(self, **kwargs) -> None:
        print('SlackbotCompletionFunction: init')

    def __call__(self, prompt, **kwargs) -> SlackBotCompletionResult:
        response = chain(prompt)
        formattedResp = format_query_response_with_sources(response, os.environ['FALLBACK_RESPONSE'])
        return SlackBotCompletionResult(formattedResp)

if __name__ == "__main__":
    complfn = SlackbotCompletionFunction()
    while True:
        prompt = input("Give prompt:")
        if (prompt == 'q'):
            break
        print(complfn(prompt).get_completions()[0])
    