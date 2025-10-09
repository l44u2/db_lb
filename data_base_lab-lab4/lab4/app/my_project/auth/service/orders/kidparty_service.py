from my_project.auth.dao import kidparty_dao
from my_project.auth.service.general_service import GeneralService

class KidpartyService(GeneralService):
    _dao = kidparty_dao