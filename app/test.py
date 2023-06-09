
import os
from .slackbot.response_formatter import format_query_response_with_sources
from .query_ai.langchain_loader import load

chain = load()
chain.return_source_documents = True

while True:
    query = input("Question:\n")
    if (query == 'q'):
        break
    response = chain(query)
    print(response)
    print(format_query_response_with_sources(response, os.environ['FALLBACK_RESPONSE']))

