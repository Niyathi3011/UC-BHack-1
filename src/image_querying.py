from pathlib import Path
from typing import Dict, List, Optional

from llama_index.readers.file.image_caption_reader import ImageCaptionReader
from llama_index.readers.schema.base import ImageDocument, Document
from llama_index.data_structs.node import Node

from llama_index import (KeywordTableIndex, SimpleKeywordTableIndex, GPTKeywordTableIndex, 
                         GPTSimpleKeywordTableIndex, ListIndex, GPTListIndex, TreeIndex, GPTTreeIndex, 
                         DocumentSummaryIndex, GPTDocumentSummaryIndex, VectorStoreIndex)

from llama_index.node_parser import SimpleNodeParser
import os


class ImageIndex(ImageCaptionReader):
    def __init__(
        self,
        indexer=None
    ):
        super().__init__()
        self.indexer = None
        self.nodes = None
        self.parser = SimpleNodeParser.from_defaults(
            chunk_size=512, 
            include_extra_info=False,
            include_prev_next_rel=False,
        )
    
    def load_data(self, image, extra_info: Optional[Dict] = None):
        img_doc:ImageDocument = super().load_data(image, extra_info)  # image has been captioned
        caption = img_doc[0].get_text()  # caption extracted
        if self.indexer == None:
            self.indexer = VectorStoreIndex.from_documents([Document(caption)])
            self.retriever = self.indexer.as_query_engine()
        else:
            nodes = self.parser.get_nodes_from_documents([Document(caption)])
            self.indexer.insert_nodes(nodes)
            self.__refresh_retriever()
    
    def __refresh_retriever(self):
        self.retriever = self.indexer.as_query_engine()
    
    def query(self, query_str):
        return self.retriever.query(query_str)
    
    def retrieve(self, retrieve_str):
        return self.retriever.retrieve(retrieve_str)
    
    def load_data_dir(self, dir_path):
        images = os.listdir(dir_path)
        for i in images:
            self.load_data(os.path.join(dir_path, i))
        self.__refresh_retriever()