from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto

class EventKidParty(db.Model, IDto):
    __tablename__ = "event_kidparty"

    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), primary_key=True)
    kidparty_id = db.Column(db.Integer, db.ForeignKey('kidparty.id'), primary_key=True)

    event = db.relationship("Event", back_populates="event_kidparties")
    kidparty = db.relationship("KidParty", back_populates="event_kidparties")

    def __repr__(self) -> str:
        return f"EventKidParty({self.event_id}, {self.kidparty_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "event_id": self.event_id,
            "kidparty_id": self.kidparty_id
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> EventKidParty:
        obj = EventKidParty(**dto_dict)
        return obj