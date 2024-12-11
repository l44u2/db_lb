from typing import List
from my_project.auth.dao import event_wedding_dao
from my_project.auth.service.general_service import GeneralService

class EventWeddingService(GeneralService):
    _dao = event_wedding_dao