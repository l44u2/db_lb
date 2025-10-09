from my_project.auth.dao import firstsep_dao
from my_project.auth.service.general_service import GeneralService

class FirstsepService(GeneralService):
    _dao = firstsep_dao