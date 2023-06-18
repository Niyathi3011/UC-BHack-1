from pathlib import Path
from arxiv_engine.utils import ArxivWrapper
from arxiv_engine.server_config import BASE_DATABASE_PATH
from llama_index import download_loader

PDFReader = download_loader("PDFReader")
loader = PDFReader()

arxiv_wrapper = ArxivWrapper()
title_categories_dict = arxiv_wrapper.download_datasets()
print(title_categories_dict)

def load_document_in_llama(title_categories_dict):
    categories_text_dict = {}
    # documents_list = []
    for title, categories in title_categories_dict.items():
        print(title, categories)
        file_path = BASE_DATABASE_PATH + categories + "/" + title + ".pdf"
        print(file_path)
        documents = loader.load_data(file=Path(file_path))
        print(documents)
        # documents_list.append(documents)
        categories_text_dict[categories] = documents
    return categories_text_dict

def get_text_data(categories_text_dict):
    document_text_dict = {}
    for category, documents in categories_text_dict.items():
        documents_text = ""
        for pages in documents:
            documents_text = documents_text + pages.get_text() + " "
        title = pages.extra_info['file_name']
        document_text_dict[title] = {
            'document_text': documents_text,
            'category': category
        }
    return document_text_dict

categories_text_dict = load_document_in_llama(title_categories_dict)
document_text_dict = get_text_data(categories_text_dict)

print(document_text_dict)