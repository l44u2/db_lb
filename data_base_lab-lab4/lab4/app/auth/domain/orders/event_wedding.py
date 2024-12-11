from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto

class EventWedding(db.Model, IDto):
    __tablename__ = "event_wedding"

    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), primary_key=True)
    wedding_id = db.Column(db.Integer, db.ForeignKey('wedding.id'), primary_key=True)

    event = db.relationship("Event", back_populates="event_weddings")
    wedding = db.relationship("Wedding", back_populates="event_weddings")

    def __repr__(self) -> str:
        return f"EventWedding({self.event_id}, {self.wedding_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "event_id": self.event_id,
            "wedding_id": self.wedding_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> EventWedding:
        obj = EventWedding(**dto_dict)
        return obj