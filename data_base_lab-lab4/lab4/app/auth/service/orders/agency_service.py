from typing import List
from my_project.auth.dao import agency_dao
from my_project.auth.service.general_service import GeneralService

class AgencyService(GeneralService):
    _dao = agency_dao

    def get_events_after_agency(self, agency_id: int) -> List[object]:
        return self._dao.get_events_after_agency(agency_id)

    def get_agencies_after_speciality(self, speciality_id: int) -> List[object]:
        return self._dao.get_agencies_after_speciality(speciality_id)