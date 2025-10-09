from my_project.auth.service import birthday_service
from my_project.auth.controller.general_controller import GeneralController

class BirthdayController(GeneralController):
    _service = birthday_service