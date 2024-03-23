from skills.basic_skill import BasicSkill

# Import Amazon API library
import amazonapi

# Define the class for the new skill

class AmazonShoppingSkill(BasicSkill):
    def __init__(self):
        self.name = 'Amazon Shopping'
        self.metadata = {
            'name': self.name,
            'description': 'This skill allows you to shop for stuff on Amazon',
            'parameters': {
                'type': 'object',
                'properties': {
                    'item': {
                        'type': 'string',
                        'description': 'The item you want to purchase'
                    },
                    'quantity': {
                        'type': 'integer',
                        'description': 'The quantity of the item'
                    }
                },
                'required': ['item', 'quantity']
            }
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, item, quantity):
        # Initialize the Amazon API
        amazon = amazonapi.AmazonAPI()
        # Call the shopping method in the Amazon API
        result = amazon.shop(item, quantity)
        return f'You have successfully purchased {quantity} {item} from Amazon!'