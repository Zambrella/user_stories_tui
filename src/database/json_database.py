from typing import List, Optional
from database.base_database import BaseDatabase
from domain.user_story import UserStory
import json
import os

STORAGE_LOCATION = "data/user_stories.json"
DIRECTORY = "data"

class JsonDatabase(BaseDatabase):

    def __init__(self) -> None:
        dir_exists = os.path.exists(DIRECTORY)
        if not dir_exists:
            os.makedirs(DIRECTORY)

    def get_all_stories(self) -> Optional[List[UserStory]]:
        try:
            with open(STORAGE_LOCATION, "r") as file:
                data = json.load(file)
                stories = []
                for story in data:
                    stories.append(UserStory.from_dict(story))
                if len(stories) == 0:
                    return None
                return stories
        except IOError:
            return None

        
    def get_story(self, story_id: str) -> Optional[UserStory]:
        all_stories = self.get_all_stories()
        if all_stories is None:
            return None
        return list(filter(lambda x: x.id == story_id, all_stories))[0]

    def save_user_story(self, story: UserStory) -> None:
        try:
            # Get all stories
            all_stories = self.get_all_stories()

            # If there is nothing saved create a new list with the single story
            if all_stories is None:
                stories = [story.to_dict()]
                data = json.dumps(stories)
                with open(STORAGE_LOCATION, "w") as file:
                    file.write(data)
            else:
                for i, item in enumerate(all_stories):
                    if story.id not in [story.id for story in all_stories]:
                        all_stories.append(story)
                    else:
                        # If the old item id matches new id then it needs to be replaced in the same location
                        if item.id == story.id:
                            all_stories[i] = story

                data = json.dumps([story.to_dict() for story in all_stories])
                with open(STORAGE_LOCATION, "w") as file:
                    file.write(data)
        except Exception as error:
            print("Error here")
            print(error)
            raise
            

    def update_user_story(self, story: UserStory) -> None:
        self.save_user_story(story)

    def delete_user_story(self, story_id: str) -> None:
        try:
            all_stories = self.get_all_stories()

            if all_stories is None:
                pass
            else:
                updated_list = [story for story in all_stories if story.id != story_id]
                data = json.dumps([story.to_dict() for story in updated_list])
                with open(STORAGE_LOCATION, "w") as file:
                    file.write(data)
        except Exception as error:
            print(error)
            raise
