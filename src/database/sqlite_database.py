import sqlite3
from database.base_database import BaseDatabase
from domain.user_story import UserStory
from typing import List


class SQLiteDatabase(BaseDatabase):

    STORIES_DATABASE = "stories.db"

    def __init__(self) -> None:
        self.con = sqlite3.connect(self.STORIES_DATABASE)
        cur = self.con.cursor()
        # See if table exists in master
        result = cur.execute(
            """
            SELECT name FROM sqlite_master WHERE name="stories"
            """
        )
        # if it doesn't exist then create it
        if result.fetchone() is None:
            cur.execute(
                """
                CREATE TABLE stories(id, score, subject, want, reason)
                """
            )

    def __del__(self):
        self.con.close()

    def get_all_stories(self) -> List[UserStory]:
        cur = self.con.cursor()
        result = cur.execute(
            """
            SELECT * FROM stories
            """
        )
        data = result.fetchall()
        return [UserStory(id=row[0], score=row[1], subject=row[2], want=row[3], reason=row[4]) for row in data]

    def get_story(self, story: str) -> UserStory:
        cur = self.con.cursor()
        result = cur.execute(
            """
            SELECT * FROM stories WHERE id=?
            """,
            story
        )
        data = result.fetchone()
        return UserStory(id=data[0], score=data[1], subject=data[2], want=data[3], reason=data[4])

    def save_user_story(self, story: UserStory) -> None:
        cur = self.con.cursor()
        cur.execute(
            """
            INSERT INTO stories VALUES
            (?, ?, ?, ?, ?)
            """,
            (story.id, story.score, story.subject, story.want, story.reason)
        )
        self.con.commit()

    def update_user_story(self, story: UserStory) -> None:
        pass

    def delete_user_story(self, story_id: str) -> None:
        cur = self.con.cursor()
        cur.execute(
            """
            DELETE FROM stories WHERE id=?
            """,
            (story_id,)
        )
        self.con.commit()

    def clear(self) -> None:
        cur = self.con.cursor()
        cur.execute(
            """
            DELETE FROM stories
            """
        )
        self.con.commit()
