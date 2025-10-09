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

@event_birthday_bp.get('/event/<int:event_id>')
@swag_from({
    'tags': ['EventBirthday'],
    'summary': 'Get Birthday mapping by Event ID',
    'parameters': [{'name': 'event_id', 'in': 'path', 'type': 'integer', 'required': True}],
    'responses': {200: {'description': 'List of Birthday IDs for the given Event'}}
})
def get_birthday_by_event(event_id: int) -> Response:
    return make_response(jsonify(event_birthday_controller.get_birthday_after_event(event_id)), HTTPStatus.OK)

@event_birthday_bp.get('/birthday/<int:birthday_id>')
@swag_from({
    'tags': ['EventBirthday'],
    'summary': 'Get Event mapping by Birthday ID',
    'parameters': [{'name': 'birthday_id', 'in': 'path', 'type': 'integer', 'required': True}],
    'responses': {200: {'description': 'List of Event IDs for the given Birthday'}}
})
def get_event_by_birthday(birthday_id: int) -> Response:
    return make_response(jsonify(event_birthday_controller.get_event_after_birthday(birthday_id)), HTTPStatus.OK)

@event_birthday_bp.delete('/<int:event_id>/<int:birthday_id>')
@swag_from({
    'tags': ['EventBirthday'],
    'summary': 'Delete Event-Birthday mapping',
    'parameters': [
        {'name': 'event_id', 'in': 'path', 'type': 'integer', 'required': True},
        {'name': 'birthday_id', 'in': 'path', 'type': 'integer', 'required': True}
    ],
    'responses': {200: {'description': 'Mapping deleted successfully'}}
})
def delete_event_birthday(event_id: int, birthday_id: int) -> Response:
    event_birthday_controller.delete_by_ids(event_id, birthday_id)
    return make_response("Event birthday mapping deleted", HTTPStatus.OK)
