from typing import List
from my_project.auth.service import event_birthday_service
from my_project.auth.controller.general_controller import GeneralController

class EventBirthdayController(GeneralController):
    _service = event_birthday_service

    def get_birthday_after_event(self, event_id: int) -> List[object]:
        return self._service.get_birthday_after_event(event_id)

    def get_event_after_birthday(self, birthday_id: int) -> List[object]:
        return self._service.get_event_after_birthday(birthday_id)