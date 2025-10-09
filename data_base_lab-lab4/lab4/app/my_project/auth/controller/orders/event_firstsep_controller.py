from typing import List
from my_project.auth.service import event_firstsep_service
from my_project.auth.controller.general_controller import GeneralController

class EventFirstSepController(GeneralController):
    _service = event_firstsep_service

    def get_firstsep_after_event(self, event_id: int) -> List[object]:
        return self._service.get_firstsep_after_event(event_id)

    def get_event_after_firstsep(self, firstsep_id: int) -> List[object]:
        return self._service.get_event_after_firstsep(firstsep_id)