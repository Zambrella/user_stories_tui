from typing import List 

from domain.user_story import UserStory


class CliUi:

    def __init__(self) -> None:
        pass

    def display_no_results(self):
        print("No saved user stories")

    def display_story_list(self, stories: List[UserStory]):
        if stories is None:
            print("There are no stories")
        else:
            print("User stories:")
            for story in stories:
                print(f"{str(story)} - Score: {story.score}")

    def display_error(self, error: str):
        print(f"Error: {error}")
