from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto

class Christmass(db.Model, IDto):
    __tablename__ = "christmass"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    event_date = db.Column(db.Date, nullable=False)
    duration = db.Column(db.Time, nullable=False)
    value = db.Column(db.Numeric, nullable=False)

    event_christmasses = db.relationship("EventChristmass", back_populates="christmass", lazy='dynamic')

    def __repr__(self) -> str:
        return f"Christmass({self.id}, '{self.event_date}', '{self.duration}', {self.value})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "event_date": self.event_date.isoformat(),
            "duration": self.duration.strftime('%H:%M:%S'),
            "value": str(self.value)
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Christmass:
        obj = Christmass(**dto_dict)
        return obj