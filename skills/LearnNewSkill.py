import os
from skills.basic_skill import BasicSkill

class LearnNewSkill(BasicSkill):
    def __init__(self):
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
                        "description": """The Python code that is behind the new skill. the code should follow the following template:
from skills.basic_skill import Basic Skill
{import any other libraries}
class {name of the new skill} (BasicSkill):
    def __init__(self):
        self.name = {skill name}
        self.metadata = {
            \"name\": self.name,
            \"description\": \"{a description of the skill that describes when it should be used and what it does}\",
            \"parameters\": {
                \"type\": \"object\",
                \"properties\": {
                    \"{parameter 1 name}\": {
                        \"type\": {parameter type, i.e: string}\",
                        \"description\": \"{description of what the parameter is used for}\"
                    },
                    \"{parameter 2 name}\": {
                        \"type\": {parameter type, i.e: string}\",
                        \"description\": \"{description of what the parameter is used for}\"
                    }
                },
                \"required\": [\"{name of required parameter}\", \"{name of required parameter}\"]
            }
        }
        super().__init__(name=self.name, metadata=self.metadata)
    
    def perform(self, {parameters}):
        {skill functionality}
        return {string that describes the result of the function}
"""
                    }
                },
                "required": ["skill_name", "python_implementation"]
            }
        }

        super().__init__(name=self.name, metadata=self.metadata)
    
    def perform(self, skill_name, python_implementation):
        file_name = f"{skill_name}.py"
        file_path = os.path.join("skills", file_name)
        try: 
            with open(file_path, 'w') as file:
                file.write(python_implementation)
                return f"Successfully created {file_name}.py"
        except Exception as error:
            return f"Failed to create {file_name}.py: {error}"