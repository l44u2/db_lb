from typing import List
from my_project.auth.dao import animator_dao
from my_project.auth.service.general_service import GeneralService

class AnimatorService(GeneralService):
    _dao = animator_dao

    def get_events_after_animator(self, animator_id: int) -> List[object]:
        return self._dao.get_events_after_animator(animator_id)