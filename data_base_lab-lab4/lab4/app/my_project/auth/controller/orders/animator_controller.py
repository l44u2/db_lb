from typing import List
from my_project.auth.service import animator_service
from my_project.auth.controller.general_controller import GeneralController

class AnimatorController(GeneralController):
    _service = animator_service

    def get_animators_by_name(self, name: str) -> List[object]:
        return self._service.get_animators_by_name(name)

    def get_animators_by_surname(self, surname: str) -> List[object]:
        return self._service.get_animators_by_surname(surname)