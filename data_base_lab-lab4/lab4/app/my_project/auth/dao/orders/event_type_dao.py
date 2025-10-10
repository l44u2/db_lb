from typing import List, Dict, Any
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.event_type import EventType
import sqlalchemy

class TypeDAO(GeneralDAO):
    _domain_type = EventType

    def get_types_by_name(self, type_name: str) -> List[Dict[str, Any]]:
        result = self._session.execute(
            sqlalchemy.text("""
                SELECT * FROM type 
                WHERE type LIKE :type_name
            """),
            {"type_name": f"%{type_name}%"}
        ).mappings().all()
        return [dict(row) for row in result]

    def get_types_with_events(self) -> List[Dict[str, Any]]: 
        result = self._session.execute(
            sqlalchemy.text("""
                SELECT t.* FROM type t
                JOIN event e ON t.id = e.type_id
                GROUP BY t.id
            """)
        ).mappings().all()
        return [dict(row) for row in result]
