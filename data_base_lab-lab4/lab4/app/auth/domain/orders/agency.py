from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Agency(db.Model, IDto):
    __tablename__ = "agency"

    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=True)
    speciality_id = db.Column(db.Integer, db.ForeignKey('speciality.id'), nullable=False)

    speciality = db.relationship("Speciality", back_populates="agencies")
    events = db.relationship("Event", back_populates="agency", lazy='dynamic')

    def __repr__(self) -> str:
        return f"Agency({self.id}, '{self.name}', {self.speciality_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "speciality_id": self.speciality_id,
            "speciality_type": self.speciality.speciality_type,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Agency:
        obj = Agency(**dto_dict)
        return obj