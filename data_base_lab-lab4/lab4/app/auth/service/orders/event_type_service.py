from typing import List
from my_project.auth.dao import type_dao
from my_project.auth.service.general_service import GeneralService

class TypeService(GeneralService):
    _dao = type_dao

    def get_events_after_type(self, type_id: int) -> List[object]:
        return self._dao.get_events_after_type(type_id)
        
    def get_type_after_event(self, event_id: int) -> List[object]:
        return self._dao.get_type_after_event(event_id)