from typing import List
from my_project.auth.service import firstsep_service
from my_project.auth.controller.general_controller import GeneralController

class FirstSepController(GeneralController):
    _service = firstsep_service

    def get_firstsep_by_date(self, date: str) -> List[object]:
        return self._service.get_firstsep_by_date(date)

    def get_firstsep_by_duration(self, duration: str) -> List[object]:
        return self._service.get_firstsep_by_duration(duration)

    def get_firstsep_by_value(self, value: float) -> List[object]:
        return self._service.get_firstsep_by_value(value)