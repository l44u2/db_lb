from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto

class EventFirstSep(db.Model, IDto):
    __tablename__ = "event_firstsep"

    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), primary_key=True)
    firstsep_id = db.Column(db.Integer, db.ForeignKey('firstsep.id'), primary_key=True)

    event = db.relationship("Event", back_populates="event_firstseps")
    firstsep = db.relationship("FirstSep", back_populates="event_firstseps")

    def __repr__(self) -> str:
        return f"EventFirstSep({self.event_id}, {self.firstsep_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "event_id": self.event_id,
            "firstsep_id": self.firstsep_id
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> EventFirstSep:
        obj = EventFirstSep(**dto_dict)
        return obj