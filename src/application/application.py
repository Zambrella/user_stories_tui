from database.json_database import JsonDatabase
from ui.cli_ui import CliUi


class Application:
    
    def __init__(self) -> None:
        self.database = JsonDatabase()
        self.ui = CliUi()

    def get_all_stories(self, descending: bool = False) -> None:
        try:
            all_stories = self.database.get_all_stories()
            if all_stories is None:
                self.ui.display_no_results()
            else:
                all_stories.sort(key=lambda x: x.score or 0, reverse=descending)
                self.ui.display_story_list(all_stories)
        except Exception as e:
            self.ui.display_error(str(e))

    def add_story(self) -> None:
        try:
            new_story = self.ui.add_story()
            self.database.save_user_story(new_story)
        except Exception as e:
            self.ui.display_error(str(e))
            
    def delete_story(self) -> None:
        try:
            all_stories = self.database.get_all_stories()
            if all_stories is None:
                self.ui.display_no_results()
            else:
                story_to_delete = self.ui.delete_story(all_stories)
                self.database.delete_user_story(story_to_delete.id)
                self.ui.delete_success()
        except Exception as e:
            self.ui.display_error(str(e))
