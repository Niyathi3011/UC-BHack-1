from pathlib import Path
from arxiv_engine.utils import ArxivWrapper
from arxiv_engine.server_config import BASE_DATABASE_PATH
from llama_index import download_loader

PDFReader = download_loader("PDFReader")
loader = PDFReader()

arxiv_wrapper = ArxivWrapper()
title_categories_dict = arxiv_wrapper.download_datasets()
print(title_categories_dict)
for title, categories in title_categories_dict.items():
    print(title, categories)
    file_path = BASE_DATABASE_PATH + categories + "/" + title + ".pdf"
    print(file_path)
    documents = loader.load_data(file=Path(file_path))
    print(documents)