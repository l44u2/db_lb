from typing import List, Dict, Any
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.wedding import Wedding
import sqlalchemy

class WeddingDAO(GeneralDAO):
    _domain_type = Wedding

    def get_weddings_by_date(self, date: str) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_weddings_by_date(:p1)"),
                                     {"p1": date}).mappings().all()
        return [dict(row) for row in result]