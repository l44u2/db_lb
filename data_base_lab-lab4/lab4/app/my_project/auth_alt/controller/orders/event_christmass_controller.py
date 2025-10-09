from typing import List
from my_project.auth.service import event_christmass_service
from my_project.auth.controller.general_controller import GeneralController

class EventChristmasController(GeneralController):
    _service = event_christmass_service

    def get_christmass_after_event(self, event_id: int) -> List[object]:
        return self._service.get_christmass_after_event(event_id)

    def get_event_after_christmass(self, christmass_id: int) -> List[object]:
        return self._service.get_event_after_christmass(christmass_id)