from typing import List 
from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
from domain import user_story

from domain.user_story import UserStory


class CliUi:

    def __init__(self) -> None:
        self.console = Console()

    def display_no_results(self):
        self.console.print("[orange1]No saved user stories[/]")

    def display_story_list(self, stories: List[UserStory]):
        if stories is None:
            self.display_no_results()
        else:
            total_score = 0
            table = Table(title="User Stories")
            table.add_column("Story", justify="left", style="yellow")
            table.add_column("Score", justify="center", style="cyan2")
            for story in stories:
                total_score += story.score or 0
                table.add_row(CliUi.print_story(story), str(story.score))
            self.console.print(table)
            self.console.print(f"[bold]Total score: [cyan2]{total_score}[/]")

    def display_error(self, error: str):
        self.console.print(f"[red bold]Error[/]: [red]{error}[/]")

    def add_story(self) -> UserStory:
        self.console.print("Who is the [bold yellow]subject[/]? (e.g. user, stakeholder)")
        subject = Prompt.ask("As a")
        self.console.print("\nWhat do they want to do?")
        want = Prompt.ask(f"As a [bold yellow]{subject}[/], I want to")
        self.console.print(f"\nWhat is the reason for wanting to [bold yellow]{want}[/]")
        reason = Prompt.ask(f"As a [bold yellow]{subject}[/], I want to [bold yellow]{want}[/], so that")
        score = None
        while True:
            add_score = Prompt.ask("Would you like to add a [bold yellow]score[/]?", choices=["y", "n"]).upper()
            if add_score == "Y":
                score = Prompt.ask("What is the score?")
                try:
                    score = int(score)
                    break
                except:
                    self.console.print("[red]Invalid input")
                    continue
            elif add_score == "N":
                break
            else:
                self.console.print("[red]Invalid input")
                continue

        if score:
            return UserStory(subject=subject, want=want, reason=reason, score=score)
        else:
            return UserStory(subject=subject, want=want, reason=reason)

    def add_success(self, story: UserStory):
        self.console.print("[green]User story added successfully\n[/]")
        self.console.print(CliUi.print_story(story))
        

    def delete_story(self, stories: List[UserStory]) -> UserStory:
        table = Table(title="User Stories")
        table.add_column("Id", justify="center", style="orange1")
        table.add_column("Story", justify="left", style="yellow")
        table.add_column("Score", justify="center", style="cyan2")
        for i, story in enumerate(stories):
            table.add_row(str(i), CliUi.print_story(story), str(story.score))
        self.console.print(table)
        user_choice = Prompt.ask("Pick a story [orange1]ID[/] to delete")
        if int(user_choice) < len(stories):
            return stories[int(user_choice)]
        else:
            raise IndexError("Invalid option")

    def delete_success(self):
        self.console.print("[green]User story deleted.[/]")

    def clear_confirm(self) -> bool:
        confirmation = Prompt.ask("Are you sure you want [orange1]to delete all user stories[/]?", choices=["y", "n"]).upper()
        return confirmation == "Y"

    def clear_success(self):
        self.console.print("[green]User stories deleted.[/]")

    @staticmethod
    def print_story(story: UserStory) -> str:
        return f"{user_story.FIRST_PART} [bold]{story.subject}[/], {user_story.SECOND_PART} [bold]{story.want}[/], {user_story.THIRD_PART} [bold]{story.reason}[/]"
