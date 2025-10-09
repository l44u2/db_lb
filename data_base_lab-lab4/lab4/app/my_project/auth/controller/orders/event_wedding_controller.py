from typing import List
from my_project.auth.service import event_wedding_service
from my_project.auth.controller.general_controller import GeneralController

class EventWeddingController(GeneralController):
    _service = event_wedding_service

    def get_wedding_after_event(self, event_id: int) -> List[object]:
        return self._service.get_wedding_after_event(event_id)

    def get_event_after_wedding(self, wedding_id: int) -> List[object]:
        return self._service.get_event_after_wedding(wedding_id)