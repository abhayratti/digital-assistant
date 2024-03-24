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

    def perform(self, query):
        headers = {'User-Agent': 'Mozilla/5.0'}
        url = f"https://www.ebay.com/sch/i.html?_nkw={query}"
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        items = soup.find_all('li', {'class': 's-item'})[:5]  # get top 5 items

        results = []
        for item in items:
            title = item.find('h3', {'class': 's-item__title'}).text
            price = item.find('span', {'class': 's-item__price'}).text
            link = item.find('a', {'class': 's-item__link'})['href']
            results.append(f'{title} - {price} - {link}')

        return '\n'.join(results)