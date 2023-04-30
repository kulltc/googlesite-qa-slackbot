from langchain.document_loaders import UnstructuredMarkdownLoader
from langchain.document_loaders import DirectoryLoader
from langchain.indexes import VectorstoreIndexCreator

def setup_loader_and_index():
    loader = DirectoryLoader("./data/site_contents/", glob="**/*.md", loader_cls=UnstructuredMarkdownLoader, silent_errors=True)
    index = VectorstoreIndexCreator().from_loaders([loader])
    return index
