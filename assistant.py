from openai import OpenAI
import json
import os
import sys

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
                model="gpt-3.5-turbo",
                messages=self.conversation_transcript,
                # functions: this parameter is a list 
                functions=self.get_skill_metadata(),
                function_call="auto"
            )
            return response

    def get_response(self, prompt):      
        self.add_msg_to_transcript("user", prompt)

        while True:
            response = self.get_openai_response()

            assistant_msg = response.choices[0].message
            msg_contents = assistant_msg.content

            if not assistant_msg.function_call:
                self.conversation_transcript.append(msg_contents)
                return msg_contents
        
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
        
