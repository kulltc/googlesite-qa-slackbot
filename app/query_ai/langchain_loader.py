
from langchain.document_loaders import UnstructuredMarkdownLoader
from langchain.document_loaders import DirectoryLoader
from langchain.chains.qa_with_sources.retrieval import RetrievalQAWithSourcesChain
from langchain.chains import RetrievalQA
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores.chroma import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.llms import OpenAI
from query_ai.prompt import PROMPT
import os

def load():
    loader = DirectoryLoader("./data/site_contents/", glob="**/*.md", loader_cls=UnstructuredMarkdownLoader, silent_errors=True)
    docs = []
    docs.extend(loader.load())
    sub_docs = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0).split_documents(docs)
    embeddings = OpenAIEmbeddings()
    docsearch = Chroma.from_documents(sub_docs, embeddings)
    chain_type_kwargs = {"prompt": PROMPT}
    chain = RetrievalQA.from_chain_type(
        OpenAI(model_name=os.environ['OPENAI_MODEL']),
        chain_type="stuff",
        retriever=docsearch.as_retriever(),
        chain_type_kwargs=chain_type_kwargs
    )
    chain.return_source_documents = True
    return chain