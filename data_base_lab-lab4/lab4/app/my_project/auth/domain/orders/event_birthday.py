from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto

class EventBirthday(db.Model, IDto):
    __tablename__ = "event_birthday"

    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), primary_key=True)
    birthday_id = db.Column(db.Integer, db.ForeignKey('birthday.id'), primary_key=True)

    event = db.relationship("Event", back_populates="event_birthdays")
    birthday = db.relationship("Birthday", back_populates="event_birthdays")

    def __repr__(self) -> str:
        return f"EventBirthday({self.event_id}, {self.birthday_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "event_id": self.event_id,
            "birthday_id": self.birthday_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> EventBirthday:
        obj = EventBirthday(**dto_dict)
        return obj