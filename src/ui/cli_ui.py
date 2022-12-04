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

    def add_story(self) -> UserStory:
        print("Fill in the blanks\n")
        subject = input("As a ___ ")
        want = input(f"As a {subject}, I want to ___ ")
        reason = input(f"As a {subject}, I want to {want}, so that ___ ")
        score = None
        while True:
            add_score = input("Would you like to add a score? [y/n] ").upper()
            if add_score == "Y":
                score = input("What is the score? ")
                try:
                    score = int(score)
                    break
                except:
                    print("Invalid input")
                    continue
            elif add_score == "N":
                break
            else:
                print("Invalid input.")
                continue

        if score:
            return UserStory(subject=subject, want=want, reason=reason, score=score)
        else:
            return UserStory(subject=subject, want=want, reason=reason)
