from skills.basic_skill import BasicSkill
import pytwhatkit

class PlayYoutubeVideo(BasicSkill):
    def __init__(self, name, metadata):
        self.name = "PlayYoutubeVideo"
        self.metadata = {
            "name": self.name,
            "description": "Plays a Youtube Video based on its titles",
            "parameters": {
                "video_title": {
                    "type": "string",
                    "description": "Name of the Youtube video"
                }
            },
            "required": ["video_title"]
        }
        super().__init__(self.name, self.metadata)

    def perform(self, video_title):
        try:
            pytwhatkit.playonyt(video_title)
            return f"Successfully Played {video_title}"
        except:
            return f"Can't play {video_title}"