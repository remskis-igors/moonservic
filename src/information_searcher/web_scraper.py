import requests
from bs4 import BeautifulSoup


class WebScraper:
    def scrape_page(self, url):
        # Send GET request to URL
        response = requests.get(url)

        # Parse HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")

        # Extract relevant information from HTML
        title = soup.find("title").text.strip()
        summary = soup.find("meta", attrs={"name": "description"})["content"]
        links = [a["href"] for a in soup.find_all("a")]

        return title, summary, links
