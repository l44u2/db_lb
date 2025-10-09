from typing import List
from my_project.auth.dao import event_christmass_dao
from my_project.auth.service.general_service import GeneralService

class EventChristmassService(GeneralService):
    _dao = event_christmass_dao