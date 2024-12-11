from typing import List, Dict, Any
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.event_wedding import EventWedding
import sqlalchemy

class EventWeddingDAO(GeneralDAO):
    _domain_type = EventWedding

    def get_weddings_for_event(self, event_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_weddings_for_event(:p1)"),
                                     {"p1": event_id}).mappings().all()
        return [dict(row) for row in result]