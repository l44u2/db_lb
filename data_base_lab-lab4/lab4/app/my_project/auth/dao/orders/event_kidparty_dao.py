from typing import List, Dict, Any
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.event_kidparty import EventKidParty
import sqlalchemy

class EventKidPartyDAO(GeneralDAO):
    _domain_type = EventKidParty

    def get_kidparty_by_event(self, event_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(
            sqlalchemy.text("""
                SELECT k.*, e.type_id 
                FROM kidparty k
                JOIN event_kidparty ek ON k.id = ek.kidparty_id
                JOIN event e ON e.id = ek.event_id
                WHERE ek.event_id = :event_id
            """),
            {"event_id": event_id}
        ).mappings().all()
        return [dict(row) for row in result]

    def get_events_by_kidparty(self, kidparty_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(
            sqlalchemy.text("""
                SELECT e.* 
                FROM event e
                JOIN event_kidparty ek ON e.id = ek.event_id
                WHERE ek.kidparty_id = :kidparty_id
            """),
            {"kidparty_id": kidparty_id}
        ).mappings().all()
        return [dict(row) for row in result]