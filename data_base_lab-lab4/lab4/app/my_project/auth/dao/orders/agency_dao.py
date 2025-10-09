from typing import List, Dict, Any
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.agency import Agency
import sqlalchemy

class AgencyDAO(GeneralDAO):
    _domain_type = Agency
    
    def get_agencies_by_speciality(self, speciality_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_agencies_by_speciality(:p1)"),
                                     {"p1": speciality_id}).mappings().all()
        return [dict(row) for row in result]