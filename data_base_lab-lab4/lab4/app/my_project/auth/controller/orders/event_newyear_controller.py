from typing import List
from my_project.auth.service import event_newyear_service
from my_project.auth.controller.general_controller import GeneralController

class EventNewYearController(GeneralController):
    _service = event_newyear_service

    def get_newyear_after_event(self, event_id: int) -> List[object]:
        return self._service.get_newyear_after_event(event_id)

    def get_event_after_newyear(self, newyear_id: int) -> List[object]:
        return self._service.get_event_after_newyear(newyear_id)