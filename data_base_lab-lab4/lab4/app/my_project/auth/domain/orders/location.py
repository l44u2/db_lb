from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Location(db.Model, IDto):
    __tablename__ = "location"

    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    house = db.Column(db.String(45), nullable=False)
    street = db.Column(db.String(45), nullable=False)

    events = db.relationship("Event", back_populates="location", lazy='dynamic')

    def __repr__(self) -> str:
        return f"Location({self.id}, '{self.house}', '{self.street}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "house": self.house,
            "street": self.street,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Location:
        obj = Location(**dto_dict)
        return obj