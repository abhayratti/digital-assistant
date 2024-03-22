from skills.basic_skill import BasicSkill

class LearnNewSkill(BasicSkill):
    def __init__(self, name, metadata):
        self.name = "LearnNewSkill"
        self.metadata = {
            "name": self.name,
            "description": "Creates a new python file for a specified skill and allows the gpt model to perform that skill",
            "parameters": {
                "type": "object",
                "properties": {
                    "skill_name": {
                        "type": "string",
                        "description": "Name of the skill"    
                    },
                    "python_implementation": {
                        "type": "string",
                        "description": """[DESCRIPTION]"""
                    }
                },
                "required": ["skill_name", "python_implementation"]
            }
        }

        super().__init__(name=self.name, metadata=self.metadata)