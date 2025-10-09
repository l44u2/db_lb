from my_project.auth.service import wedding_service
from my_project.auth.controller.general_controller import GeneralController

class WeddingController(GeneralController):
    _service = wedding_service