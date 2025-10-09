from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Speciality(db.Model, IDto):
    __tablename__ = "speciality"

    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    speciality_type = db.Column(db.String(45), nullable=False)

    agencies = db.relationship("Agency", back_populates="speciality", lazy='dynamic')


    def __repr__(self) -> str:
        return f"Speciality({self.id}, '{self.speciality_type}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "speciality_type": self.speciality_type,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Speciality:
        obj = Speciality(**dto_dict)
        return obj