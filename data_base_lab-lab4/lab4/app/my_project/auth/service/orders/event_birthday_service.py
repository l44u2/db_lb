from typing import List
from my_project.auth.dao import event_birthday_dao
from my_project.auth.service.general_service import GeneralService

class EventBirthdayService(GeneralService):
    _dao = event_birthday_dao