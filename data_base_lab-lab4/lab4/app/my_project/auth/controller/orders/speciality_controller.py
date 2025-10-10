from my_project.auth.service.orders.speciality_service import SpecialityService
from my_project.auth.controller.general_controller import GeneralController

class SpecialityController(GeneralController):
    _service = SpecialityService()