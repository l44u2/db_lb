from typing import List, Dict, Any
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.event_christmass import EventChristmass
import sqlalchemy

class EventChristmassDAO(GeneralDAO):
    _domain_type = EventChristmass

    def get_christmass_by_event(self, event_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(
            sqlalchemy.text("""
                SELECT c.*, e.type_id 
                FROM christmass c
                JOIN event_christmass ec ON c.id = ec.christmass_id
                JOIN event e ON e.id = ec.event_id
                WHERE ec.event_id = :event_id
            """),
            {"event_id": event_id}
        ).mappings().all()
        return [dict(row) for row in result]

    def get_events_by_christmass(self, christmass_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(
            sqlalchemy.text("""
                SELECT e.* 
                FROM event e
                JOIN event_christmass ec ON e.id = ec.event_id
                WHERE ec.christmass_id = :christmass_id
            """),
            {"christmass_id": christmass_id}
        ).mappings().all()
        return [dict(row) for row in result]