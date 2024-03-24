new = {
    "name": self.name,
    "description": "{a description of the skill that describes when it should be used and what it does}",
    "parameters": {
        "type": "object",
        "properties": {
            "{parameter 1 name}": {
                "type": "{parameter type, i.e: string}",
                "description": "{description of what the parameter is used for}"
            },
            "{parameter 2 name}": {
                "type": "{parameter type, i.e: string}",
                "description": "{description of what the parameter is used for}"
            }
        },
        "required": ["{name of required parameter}", "{name of required parameter}"]
    }
}