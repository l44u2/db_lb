from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto

class KidParty(db.Model, IDto):
    __tablename__ = "kidparty"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    event_date = db.Column(db.Date, nullable=False)
    duration = db.Column(db.Time, nullable=False)
    value = db.Column(db.Numeric, nullable=False)

    event_kidparties = db.relationship("EventKidParty", back_populates="kidparty", lazy='dynamic')

    def __repr__(self) -> str:
        return f"KidParty({self.id}, '{self.event_date}', '{self.duration}', {self.value})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "event_date": self.event_date,
            "duration": self.duration,
            "value": self.value
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> KidParty:
        obj = KidParty(**dto_dict)
        return obj