from typing import List, Dict, Any
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.firstsep import FirstSep
import sqlalchemy

class FirstSepDAO(GeneralDAO):
    _domain_type = FirstSep

    def get_by_value_range(self, min_value: float, max_value: float) -> List[Dict[str, Any]]:
        result = self._session.execute(
            sqlalchemy.text("""
                SELECT * FROM firstsep 
                WHERE value BETWEEN :min AND :max
            """),
            {"min": min_value, "max": max_value}
        ).mappings().all()
        return [dict(row) for row in result]