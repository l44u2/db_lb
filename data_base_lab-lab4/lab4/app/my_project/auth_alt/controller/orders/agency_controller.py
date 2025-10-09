from typing import List
from my_project.auth.service import agency_service
from my_project.auth.controller.general_controller import GeneralController

class AgencyController(GeneralController):
    _service = agency_service

    def get_agencies_by_speciality(self, speciality_id: int) -> List[object]:
        return self._service.get_agencies_by_speciality(speciality_id)