from typing import List
from my_project.auth.dao import event_firstsep_dao
from my_project.auth.service.general_service import GeneralService

class EventFirstsepService(GeneralService):
    _dao = event_firstsep_dao