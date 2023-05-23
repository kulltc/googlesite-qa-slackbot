
from .slackbot.response_formatter import format_query_response_with_sources
from query_ai.langchain_loader import create_chroma_db, load

chroma = create_chroma_db()
print('chromadb created')
print('loading chroma from disk')

chain = load()
print(chain('What is the first sentence of the docs you see?'))
