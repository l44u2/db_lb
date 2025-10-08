from typing import List
from my_project.auth.service import event_kidparty_service
from my_project.auth.controller.general_controller import GeneralController

class EventKidPartyController(GeneralController):
    _service = event_kidparty_service

    def get_kidparty_after_event(self, event_id: int) -> List[object]:
        return self._service.get_kidparty_after_event(event_id)

    def get_event_after_kidparty(self, kidparty_id: int) -> List[object]:
        return self._service.get_event_after_kidparty(kidparty_id)