from typing import List
from my_project.auth.dao import event_newyear_dao
from my_project.auth.service.general_service import GeneralService

class EventNewyearService(GeneralService):
    _dao = event_newyear_dao