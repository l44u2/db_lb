from my_project.auth.dao import newyear_dao
from my_project.auth.service.general_service import GeneralService

class NewyearService(GeneralService):
    _dao = newyear_dao