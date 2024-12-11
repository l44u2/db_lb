from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto

class EventNewYear(db.Model, IDto):
    __tablename__ = "event_newyear"

    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), primary_key=True)
    newyear_id = db.Column(db.Integer, db.ForeignKey('newyear.id'), primary_key=True)

    event = db.relationship("Event", back_populates="event_newyears")
    newyear = db.relationship("NewYear", back_populates="event_newyears")

    def __repr__(self) -> str:
        return f"EventNewYear({self.event_id}, {self.newyear_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "event_id": self.event_id,
            "newyear_id": self.newyear_id
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> EventNewYear:
        obj = EventNewYear(**dto_dict)
        return obj