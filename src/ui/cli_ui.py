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
        print("Who is the subject? (e.g. user, stakeholder)")
        subject = input("As a ")
        print("\nWhat do they want to do?")
        want = input(f"As a {subject}, I want to ")
        print(f"\nWhat is the reason for wanting to {want}")
        reason = input(f"As a {subject}, I want to {want}, so that ")
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

    def add_success(self, story: UserStory):
        print(str(story))
        print("User story added successfully")
        

    def delete_story(self, stories: List[UserStory]) -> UserStory:
        for i, story in enumerate(stories):
            print(f"{i}. {str(story)} - Score: {story.score}")
        user_choice = int(input("Pick a story to delete: "))
        if user_choice < len(stories):
            return stories[user_choice]
        else:
            raise IndexError("Invalid option")

    def delete_success(self):
        print("User story deleted.")
