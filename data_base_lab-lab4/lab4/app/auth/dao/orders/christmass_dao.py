from typing import List, Dict, Any
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.christmass import Christmass
import sqlalchemy

class ChristmassDAO(GeneralDAO):
    _domain_type = Christmass

    def get_by_year(self, year: int) -> List[Dict[str, Any]]: 
        result = self._session.execute(
            sqlalchemy.text("""
                SELECT * FROM christmass 
                WHERE YEAR(event_date) = :year
            """),
            {"year": year}
        ).mappings().all()
        return [dict(row) for row in result]