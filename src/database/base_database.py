from abc import ABC, abstractmethod
from domain.user_story import UserStory

class BaseDatabase(ABC):
    
    @abstractmethod
    def get_all_stories(self) -> UserStory:
        pass

    @abstractmethod
    def get_story(self, story: str) -> UserStory:
        pass

    @abstractmethod
    def save_user_story(self, story: UserStory) -> None:
        pass

    @abstractmethod
    def update_user_story(self, story: UserStory) -> None:
        pass

    @abstractmethod
    def delete_user_story(self, story_id: str) -> None:
        pass

