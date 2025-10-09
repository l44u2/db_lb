from my_project.auth.service import kidparty_service
from my_project.auth.controller.general_controller import GeneralController

class KidPartyController(GeneralController):
    _service = kidparty_service