import chromadb

class ChromaDBClient:
    def __init__(self):
        self.chroma_client = chromadb.Client()
        self.chroma_collection = self.chroma_client.create_collection("axriv_documents")