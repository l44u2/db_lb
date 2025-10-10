from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Speciality(db.Model, IDto):
    __tablename__ = "speciality"

    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    speicality_type = db.Column('speicality_type', db.String(45), nullable=False)

    agencies = db.relationship("Agency", back_populates="speciality", lazy='dynamic')

    def __repr__(self) -> str:
        return f"Speciality({self.id}, '{self.speicality_type}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "speciality_type": self.speicality_type,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Speciality:
        mapped_dict = {}
        if 'speciality_type' in dto_dict:
            mapped_dict['speicality_type'] = dto_dict['speciality_type']
        if 'id' in dto_dict:
            mapped_dict['id'] = dto_dict['id']
        
        obj = Speciality(**mapped_dict)
        return obj