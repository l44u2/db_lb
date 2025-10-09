from typing import List, Dict, Any
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.kidparty import KidParty
import sqlalchemy

class KidPartyDAO(GeneralDAO):
    _domain_type = KidParty

    def get_by_date_range(self, start_date: str, end_date: str) -> List[Dict[str, Any]]:
        result = self._session.execute(
            sqlalchemy.text("""
                SELECT * FROM kidparty 
                WHERE event_date BETWEEN :start AND :end
            """),
            {"start": start_date, "end": end_date}
        ).mappings().all()
        return [dict(row) for row in result]