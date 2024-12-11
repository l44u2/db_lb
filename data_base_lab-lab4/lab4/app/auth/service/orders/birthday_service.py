from my_project.auth.dao import birthday_dao
from my_project.auth.service.general_service import GeneralService

class BirthdayService(GeneralService):
    _dao = birthday_dao