from typing import List
from my_project.auth.service import event_service
from my_project.auth.controller.general_controller import GeneralController

class EventController(GeneralController):
    _service = event_service

    def get_events_by_animator(self, animator_id: int) -> List[object]:
        return self._service.get_events_by_animator(animator_id)

    def get_events_by_agency(self, agency_id: int) -> List[object]:
        return self._service.get_events_by_agency(agency_id)

    def get_events_by_location(self, location_id: int) -> List[object]:
        return self._service.get_events_by_location(location_id)

    def get_events_by_type(self, type_id: int) -> List[object]:
        return self._service.get_events_by_type(type_id)