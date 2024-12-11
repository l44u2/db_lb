from typing import List
from my_project.auth.dao import speciality_dao
from my_project.auth.service.general_service import GeneralService

class SpecialityService(GeneralService):
    _dao = speciality_dao
    
    def get_speciality_after_agency(self, agency_id: int) -> List[object]:
        return self._dao.get_speciality_after_agency(agency_id)