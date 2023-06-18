from llama_index import VectorStoreIndex, StorageContext
from llama_index.vector_stores import ChromaVectorStore
from llama_index.data_structs.node import Node
from arxiv_engine.server_config import chromadb_client

class ChromaIndex:
    def __init__(self, nodes_list):
        self.nodes_list = nodes_list
        self.chroma_collection = chromadb_client.chroma_collection
        self.vector_store = ChromaVectorStore(chroma_collection=self.chroma_collection)
        self.storage_context = StorageContext.from_defaults(vector_store=self.vector_store)
        self._build_index()

    def _build_index(self):
        self.index = VectorStoreIndex(self.nodes_list, storage_context=self.storage_context)
        print(self.index, "This is done")
    
    def retreiver(self, query_value):
        query_engine = self.index.as_query_engine(
            chroma_collection=self.chroma_collection
        )
        response = query_engine.retrieve(query_value)
        print(response)
