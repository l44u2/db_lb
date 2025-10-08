from my_project.auth.service import christmass_service
from my_project.auth.controller.general_controller import GeneralController

class ChristmasController(GeneralController):
    _service = christmass_service

    def find_all(self):
        christmasses = self._service.find_all()
        return [christmass.put_into_dto() for christmass in christmasses]