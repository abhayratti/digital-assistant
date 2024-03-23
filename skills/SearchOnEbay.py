from skills.basic_skill import BasicSkill

# import libraries
from ebaysdk.finding import Connection
from ebaysdk.exception import ConnectionError

class SearchOnEbay(BasicSkill):
    def __init__(self):
        self.name = 'SearchOnEbay'
        self.metadata = {
            'name': self.name,
            'description': 'This skill allows the user to search for items on eBay',
            'parameters': {
                'keywords': {
                    'type': 'string',
                    'description': 'Keywords to search for on eBay'
                },
                'category_id': {
                    'type': 'string',
                    'description': 'Category ID for a specific category on eBay'
                }
            },
            'required': ['keywords']
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, keywords, category_id='0'):
        try:
            api = Connection(appid='YOUR_API_KEY_HERE', config_file=None)
            response = api.execute('findItemsByKeywords', {'keywords': keywords, 'categoryId': category_id})
            items = response.dict()['searchResult']['item']
            results = []
            for item in items:
                results.append(item['title'])
            return ', '.join(results)
        except ConnectionError as e:
            return 'An error occurred while searching on eBay: %s' % e