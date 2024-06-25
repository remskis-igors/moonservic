import requests
import json

from src.configs.inf_search_config import Config
from web_scraper import WebScraper
from nlp_utils import NLPUtils


class SearchEngine:
    def __init__(self, config):
        self.config = config
        self.web_scraper = WebScraper()
        self.nlp_utils = NLPUtils()

    def search(self, query):
        # Set up API key and search engine endpoint
        api_key = self.config["api_key"]
        endpoint = self.config["endpoint"]

        # Set up query parameters
        params = {
            "key": api_key,
            "cx": self.config["cx"],
            "q": query,
            "num": self.config["num_results"]
        }

        # Send GET request to API
        response = requests.get(endpoint, params=params)

        # Parse JSON response
        data = json.loads(response.content)

        # Extract relevant information from response
        results = data["items"]
        for result in results:
            title, summary, links = self.web_scraper.scrape_page(result["link"])
            classified_text = self.nlp_utils.text_classification(summary)
            print(f"Title: {title}")
            print(f"Summary: {summary}")
            print(f"Links: {links}")
            print(f"Classification: {classified_text}")

    if __name__ == "__main__":
        config = Config()
        search_engine = SearchEngine(config)
        query = input("Enter your search query: ")
        search_engine.search(query)