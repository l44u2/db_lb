from my_project.auth.service import newyear_service
from my_project.auth.controller.general_controller import GeneralController

class NewYearController(GeneralController):
    _service = newyear_service