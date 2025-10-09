from typing import List, Dict, Any
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.newyear import NewYear
import sqlalchemy

class NewYearDAO(GeneralDAO):
    _domain_type = NewYear

    def get_by_duration(self, min_hours: int) -> List[Dict[str, Any]]:
        result = self._session.execute(
            sqlalchemy.text("""
                SELECT * FROM newyear 
                WHERE HOUR(duration) >= :hours
            """),
            {"hours": min_hours}
        ).mappings().all()
        return [dict(row) for row in result]