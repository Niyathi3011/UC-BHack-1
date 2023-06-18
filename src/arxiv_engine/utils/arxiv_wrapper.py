import arxiv
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

MAX_RESULTS = 1

class ArxivWrapper:
    def __init__(self):
        self.categories_list = ['cs.AI', 'cs.CL']
        self.download_datasets()
    
    def download_datasets(self):
        for categories in self.categories_list:
            self.search = arxiv.Search(
                query = categories,
                max_results = MAX_RESULTS
            )
            for result in self.search.results():
                logger.info(result.title)
                logger.info(result.primary_category)
                self.download_pdf(result)
    
    def download_pdf(self, result):
        primary_category = result.primary_category.split(".")[1]
        logger.info(primary_category)
        title = result.title.replace(" ", "_")
        logger.info(title)
        result.download_pdf(dirpath="./arxiv_engine/dataset_domain/{}".format(primary_category), filename="{}.pdf".format(title))
