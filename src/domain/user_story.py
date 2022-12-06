from typing import Dict 
import uuid
import json

FIRST_PART = "As a"
SECOND_PART = "I want to"
THIRD_PART = "so that"


class UserStory:

    def __init__(self, subject: str, want: str, reason: str, **kwargs) -> None:
        self.score: int | None = kwargs.get("score")
        self.subject: str = subject
        self.want: str = want
        self.reason: str = reason
        if (kwargs.get("id") is None):
            self.id: str = str(uuid.uuid4())
        else:
            self.id = kwargs["id"]


    def update_score(self, score: int):
        self.score = score

    def __str__(self) -> str:
        return f"{FIRST_PART} {self.subject}, {SECOND_PART} {self.want}, {THIRD_PART} {self.reason}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(id: {self.id}, subject: {self.subject}, want: {self.want}, reason: {self.reason}, score: {self.score})"

    def to_json(self) -> str:
        return json.dumps(self.to_dict())

    def to_dict(self) -> Dict:
        return {
            "score": self.score,
            "subject": self.subject,
            "want": self.want,
            "reason": self.reason,
            "id": self.id,
        }

    @classmethod
    def from_json(cls, data: str):
        return UserStory.from_dict(json.loads(data))

    @classmethod
    def from_dict(cls, data: Dict):
        return cls(
            score = data.get("score"),
            subject = data["subject"],
            want = data["want"],
            reason = data["reason"],
            id = data.get("id")
        )
