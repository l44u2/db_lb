# event_birthday_route.py
from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller.orders.event_birthday_controller import EventBirthdayController
from my_project.auth.domain.orders.event_birthday import EventBirthday

event_birthday_bp = Blueprint('event_birthdays', __name__, url_prefix='/event_birthdays')
event_birthday_controller = EventBirthdayController()

@event_birthday_bp.get('')
def get_all_event_birthdays() -> Response:
    return make_response(jsonify(event_birthday_controller.find_all()), HTTPStatus.OK)

@event_birthday_bp.post('')
def create_event_birthday() -> Response:
    content = request.get_json()
    event_birthday = EventBirthday.create_from_dto(content)
    event_birthday_controller.create(event_birthday)
    return make_response(jsonify(event_birthday.put_into_dto()), HTTPStatus.CREATED)

@event_birthday_bp.get('/event/<int:event_id>')
def get_birthday_by_event(event_id: int) -> Response:
    return make_response(jsonify(event_birthday_controller.get_birthday_after_event(event_id)), HTTPStatus.OK)

@event_birthday_bp.get('/birthday/<int:birthday_id>')
def get_event_by_birthday(birthday_id: int) -> Response:
    return make_response(jsonify(event_birthday_controller.get_event_after_birthday(birthday_id)), HTTPStatus.OK)

@event_birthday_bp.delete('/<int:event_id>/<int:birthday_id>')
def delete_event_birthday(event_id: int, birthday_id: int) -> Response:
    event_birthday_controller.delete_by_ids(event_id, birthday_id)
    return make_response("Event birthday mapping deleted", HTTPStatus.OK)