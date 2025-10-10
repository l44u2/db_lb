from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from flasgger import swag_from
from my_project.auth.controller.orders.event_birthday_controller import EventBirthdayController
from my_project.auth.domain.orders.event_birthday import EventBirthday

event_birthday_bp = Blueprint('event_birthday', __name__, url_prefix='/event_birthday')
event_birthday_controller = EventBirthdayController()

@event_birthday_bp.get('')
@swag_from({
    'tags': ['EventBirthday'],
    'summary': 'Get all Event-Birthday mappings',
    'responses': {200: {'description': 'List of all Event-Birthday mappings'}}
})
def get_all_event_birthdays() -> Response:
    return make_response(jsonify(event_birthday_controller.find_all()), HTTPStatus.OK)
