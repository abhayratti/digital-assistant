from skills.basic_skill import BasicSkill
import requests
from bs4 import BeautifulSoup

class EbaySearch(BasicSkill):
    def __init__(self):
        self.name = "EbaySearch"
        self.metadata = {
            "name": self.name,
            "description": "Searches for items on Ebay based on a keyword and returns the top results.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The search keyword"
                    }
                },
                "required": ["query"]
            }
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs):
        query = kwargs.get('query', '')  # Default to an empty string if no query provided
        headers = {'User-Agent': 'Mozilla/5.0'}
        url = f"https://www.ebay.com/sch/i.html?_nkw={query}"
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        items = soup.find_all('li', {'class': 's-item'})[:5]  # get top 5 items

        results = []
        for item in items:
            title_element = item.find('h3', {'class': 's-item__title'})
            title = title_element.text if title_element else "Title not available"
            price_element = item.find('span', {'class': 's-item__price'})
            price = price_element.text if price_element else "Price not available"
            link_element = item.find('a', {'class': 's-item__link'})
            link = link_element['href'] if link_element else "Link not available"
            results.append(f'{title} - {price} - {link}')

        return '\n'.join(results)