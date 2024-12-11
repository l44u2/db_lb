from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class EventType(db.Model, IDto):
    __tablename__ = "type"

    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    type_ = db.Column('type', db.String(45), nullable=False)

    events = db.relationship("Event", back_populates="event_type", lazy='dynamic')

    def __repr__(self) -> str:
        return f"EventType({self.id}, '{self.type_}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "type": self.type_,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> EventType:
        obj = EventType(**dto_dict)
        return obj