from skills.basic_skill import BasicSkill
import pywhatkit

class PlayYoutubeVideo(BasicSkill):
    def __init__(self):
        self.name = "PlayYoutubeVideo"
        self.metadata = {
            "name": self.name,
            "description": "Plays a Youtube Video based on its titles",
            "parameters": {
                "type": "object",
                "properties": {
                    "video_title": {
                    "type": "string",
                    "description": "Name of the Youtube video"
                    }
                }
                
            },
            "required": ["video_title"]
        }
        super().__init__(self.name, self.metadata)

    def perform(self, video_title):
        try:
            pywhatkit.playonyt(video_title)
            return f"Successfully Played {video_title}"
        except:
            return f"Can't play {video_title}"