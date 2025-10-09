from typing import List
from my_project.auth.dao import location_dao
from my_project.auth.service.general_service import GeneralService

class LocationService(GeneralService):
    _dao = location_dao

    def get_events_after_location(self, location_id: int) -> List[object]:
        return self._dao.get_events_after_location(location_id)