from my_project.auth.service import speciality_service
from my_project.auth.controller.general_controller import GeneralController

class SpecialityController(GeneralController):
    _service = speciality_service