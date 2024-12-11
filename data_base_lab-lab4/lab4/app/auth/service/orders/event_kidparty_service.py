from typing import List
from my_project.auth.dao import event_kidparty_dao
from my_project.auth.service.general_service import GeneralService

class EventKidpartyService(GeneralService):
    _dao = event_kidparty_dao