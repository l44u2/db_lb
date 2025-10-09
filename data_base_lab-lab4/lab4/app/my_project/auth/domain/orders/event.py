from __future__ import annotations
from typing import Dict, Any, List

from my_project import db
from my_project.auth.domain.i_dto import IDto

class Event(db.Model, IDto):
    __tablename__ = "event"

    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    animator_id = db.Column(db.Integer, db.ForeignKey('animator.id'), nullable=False)
    agency_id = db.Column(db.Integer, db.ForeignKey('agency.id'), nullable=False)
    location_id = db.Column(db.Integer, db.ForeignKey('location.id'), nullable=False)
    type_id = db.Column(db.Integer, db.ForeignKey('type.id'), nullable=False)

    animator = db.relationship("Animator", back_populates="events")
    agency = db.relationship("Agency", back_populates="events")
    location = db.relationship("Location", back_populates="events")
    event_type = db.relationship("EventType", back_populates="events")

    event_weddings = db.relationship("EventWedding", back_populates="event", lazy='dynamic')
    event_birthdays = db.relationship("EventBirthday", back_populates="event", lazy='dynamic')
    event_kidparties = db.relationship("EventKidParty", back_populates="event", lazy='dynamic')
    event_firstseps = db.relationship("EventFirstSep", back_populates="event", lazy='dynamic')
    event_christmasses = db.relationship("EventChristmass", back_populates="event", lazy='dynamic')
    event_newyears = db.relationship("EventNewYear", back_populates="event", lazy='dynamic')

    def __repr__(self) -> str:
        return f"Event({self.id}, {self.animator_id}, {self.agency_id}, {self.location_id}, {self.type_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "animator_id": self.animator_id,
            "animator_name": self.animator.name if self.animator else None,
            "animator_surname": self.animator.surname if self.animator else None,
            "agency_id": self.agency_id,
            "agency_name": self.agency.name if self.agency else None,
            "location_id": self.location_id,
            "house": self.location.house if self.location else None,
            "street": self.location.street if self.location else None,
            "type_id": self.type_id,
            "type": self.event_type.type_ if self.event_type else None,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Event:
        obj = Event(**dto_dict)
        return obj