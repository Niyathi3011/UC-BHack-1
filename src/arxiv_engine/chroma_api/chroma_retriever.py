from llama_index.indices.vector_store.retrievers import VectorIndexAutoRetriever
from llama_index.vector_stores.types import MetadataInfo, VectorStoreInfo

class ChromaRetriever:
    def __init__(self, index):
        self.vector_store_info = VectorStoreInfo(
            content_info='Research Paper from Computer Science Domain',
            metadata_info=[
                MetadataInfo(
                    name='category', 
                    type='str', 
                    description='Category of the research paper, one of [NLP, CV, AI]'),
            ]
        )
        self.retriever = VectorIndexAutoRetriever(index, vector_store_info=self.vector_store_info)
