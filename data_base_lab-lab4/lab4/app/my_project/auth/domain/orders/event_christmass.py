from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto

class EventChristmass(db.Model, IDto):
    __tablename__ = "event_christmass"

    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), primary_key=True)
    christmass_id = db.Column(db.Integer, db.ForeignKey('christmass.id'), primary_key=True)

    event = db.relationship("Event", back_populates="event_christmasses")
    christmass = db.relationship("Christmass", back_populates="event_christmasses")

    def __repr__(self) -> str:
        return f"EventChristmass({self.event_id}, {self.christmass_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "event_id": self.event_id,
            "christmass_id": self.christmass_id
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> EventChristmass:
        obj = EventChristmass(**dto_dict)
        return obj