import arxiv
import logging
from arxiv_engine.server_config import BASE_DATABASE_PATH

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ArxivWrapper:
    def __init__(self):
        self.MAX_RESULTS = 1
        self.categories_list = ['cs.AI', 'cs.CL']
    
    def download_datasets(self):
        title_categories_dict = {}
        for categories in self.categories_list:
            self.search = arxiv.Search(
                query = categories,
                max_results = self.MAX_RESULTS
            )
            for result in self.search.results():
                logger.info(result.title)
                logger.info(result.primary_category)
                primary_category = result.primary_category.split(".")[1]
                logger.info(primary_category)
                title = result.title.replace(" ", "_")
                logger.info(title)
                self.download_pdf(result, title, primary_category)
                title_categories_dict[title] = primary_category
        return title_categories_dict
    
    def download_pdf(self, result, title, primary_category):
        directory_path = BASE_DATABASE_PATH + "{}".format(primary_category)
        result.download_pdf(dirpath=directory_path, filename="{}.pdf".format(title))
