import json
import os
import sys
from openai import OpenAI

class Assistant():
    def __init__(self, keys_file, skill_objects):
        self.conversation_transcript = [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            }
        ]

        api_keys = ""
        with open(keys_file) as file:
            api_keys = json.load(file)
        
        self.client = OpenAI(api_key=api_keys["openai"])

        self.known_skills = self.reload_skills(skill_objects)

    def add_msg_to_transcript(self, role, content):
            msg_dict = {"role": role, "content": content}
            self.conversation_transcript.append(msg_dict)
    
    def get_openai_response(self):
            response = self.client.chat.completions.create(
                model="gpt-4-turbo-preview",
                messages=self.conversation_transcript,
                # functions: provide a list of metadata dictionaries with the functions the model can call to assist with the given task 
                functions=self.get_skill_metadata(),
                # function_call: "None" - make no function call, "Auto" - the model can automatically call functions, without explicitly being told, to help with response
                function_call="auto"
            )
            return response

    def get_response(self, prompt):      
        self.add_msg_to_transcript("user", prompt)

        while True:
            response = self.get_openai_response()

            assistant_msg = response.choices[0].message
            msg_contents = assistant_msg.content

            # case where model is explicitly told what skill to use
            if not assistant_msg.function_call:
                self.conversation_transcript.append(msg_contents)
                return msg_contents
            
            # if model needs to auto use a skill first find the name, then search for it
            skill_name = assistant_msg.function_call.name
            skill = self.known_skills.get(skill_name)

            if not skill:
                 return f"{skill_name} does not exist"
            
            skill_parameters = json.loads(assistant_msg.function_call.arguments)

            # perform the skill (result is a string)
            result = skill.perform(**skill_parameters)

            # once skill performed, model needs context to what happened 
            self.conversation_transcript.append(
                 {
                      "role": "function",
                      "name": skill_name,
                      "content": result
                 }
            )

            print(f"Performed the {skill_name} skill and got the following response: {result}")
        
    def reload_skills(self, skill_objects):
        known_skills = {}
        for skill in skill_objects:
            known_skills[skill.name] = skill

        return known_skills
    
    def get_skill_metadata(self):
        skills_metadata = []
        for skill in self.known_skills.values():
            skills_metadata.append(skill.metadata)

        return skills_metadata
        
