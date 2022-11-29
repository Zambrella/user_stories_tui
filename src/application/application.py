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
