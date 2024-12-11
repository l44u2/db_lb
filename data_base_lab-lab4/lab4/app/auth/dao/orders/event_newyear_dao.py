from typing import List, Dict, Any
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.event_newyear import EventNewYear
import sqlalchemy

class EventNewYearDAO(GeneralDAO):
    _domain_type = EventNewYear

    def get_newyear_by_event(self, event_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(
            sqlalchemy.text("""
                SELECT n.*, e.type_id 
                FROM newyear n
                JOIN event_newyear en ON n.id = en.newyear_id
                JOIN event e ON e.id = en.event_id
                WHERE en.event_id = :event_id
            """),
            {"event_id": event_id}
        ).mappings().all()
        return [dict(row) for row in result]

    def get_events_by_newyear(self, newyear_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(
            sqlalchemy.text("""
                SELECT e.* 
                FROM event e
                JOIN event_newyear en ON e.id = en.event_id
                WHERE en.newyear_id = :newyear_id
            """),
            {"newyear_id": newyear_id}
        ).mappings().all()
        return [dict(row) for row in result]