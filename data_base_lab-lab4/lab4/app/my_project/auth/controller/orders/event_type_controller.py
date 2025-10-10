from my_project.auth.service.orders.event_type_service import TypeService
from my_project.auth.controller.general_controller import GeneralController

class EventTypeController(GeneralController):
    _service = TypeService()