from llama_index.data_structs.node import Node

class NodeManager:
    def __init__(self):
        pass
    
    def construct_node(self, document_text_dict):
        nodes_list = []
        for _, document_text_with_category in document_text_dict.items():
            document_text = document_text_with_category['document_text']
            category = document_text_with_category['category']
            nodes_list.append(Node(document_text, extra_info={"category": category}))
        return nodes_list


