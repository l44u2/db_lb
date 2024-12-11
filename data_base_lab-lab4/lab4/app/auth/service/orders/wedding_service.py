from my_project.auth.dao import wedding_dao
from my_project.auth.service.general_service import GeneralService

class WeddingService(GeneralService):
    _dao = wedding_dao