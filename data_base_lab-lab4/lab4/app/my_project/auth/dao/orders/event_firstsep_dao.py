from typing import List, Dict, Any
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.event_firstsep import EventFirstSep
import sqlalchemy

class EventFirstSepDAO(GeneralDAO):
    _domain_type = EventFirstSep

    def get_firstsep_by_event(self, event_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(
            sqlalchemy.text("""
                SELECT f.*, e.type_id 
                FROM firstsep f
                JOIN event_firstsep ef ON f.id = ef.firstsep_id
                JOIN event e ON e.id = ef.event_id
                WHERE ef.event_id = :event_id
            """),
            {"event_id": event_id}
        ).mappings().all()
        return [dict(row) for row in result]

    def get_events_by_firstsep(self, firstsep_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(
            sqlalchemy.text("""
                SELECT e.* 
                FROM event e
                JOIN event_firstsep ef ON e.id = ef.event_id
                WHERE ef.firstsep_id = :firstsep_id
            """),
            {"firstsep_id": firstsep_id}
        ).mappings().all()
        return [dict(row) for row in result]