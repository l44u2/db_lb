# event_service.py 
from typing import List
from my_project.auth.dao import event_dao
from my_project.auth.service.general_service import GeneralService

class EventService(GeneralService):
    _dao = event_dao
    
    def get_events_by_date_range(self, start_date: str, end_date: str) -> List[object]:
        events = self._dao.get_events_by_date_range(start_date, end_date)
        return [event.put_into_dto() for event in events]

    def get_animator_after_event(self, event_id: int) -> List[object]:
        events = self._dao.get_animator_after_event(event_id)
        return [event.put_into_dto() for event in events]
        
    def get_agency_after_event(self, event_id: int) -> List[object]:
        events = self._dao.get_agency_after_event(event_id)
        return [event.put_into_dto() for event in events]

    def get_events_by_animator(self, animator_id: int) -> List[object]:
        events = self._dao.get_events_by_animator(animator_id)
        return [event.put_into_dto() for event in events]

    def get_events_by_agency(self, agency_id: int) -> List[object]:
        events = self._dao.get_events_by_agency(agency_id)
        return [event.put_into_dto() for event in events]

    def get_events_by_location(self, location_id: int) -> List[object]:
        events = self._dao.get_events_by_location(location_id)
        return [event.put_into_dto() for event in events]

    def get_events_by_type(self, type_id: int) -> List[object]:
        events = self._dao.get_events_by_type(type_id)
        return [event.put_into_dto() for event in events]