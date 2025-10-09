from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Animator(db.Model, IDto):
    __tablename__ = "animator"

    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=False)
    surname = db.Column(db.String(45), nullable=False)

    events = db.relationship("Event", back_populates="animator", lazy='dynamic')

    def __repr__(self) -> str:
        return f"Animator({self.id}, '{self.name}', '{self.surname}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "surname": self.surname,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Animator:
        obj = Animator(**dto_dict)
        return obj