import chromadb

class ChromaDBClient:
    def __init__(self):
        chroma_client = chromadb.Client()
        chroma_collection = chroma_client.create_collection("axriv_documents")