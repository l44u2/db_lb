# event_type_route.py
from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller.orders.event_type_controller import EventTypeController
from my_project.auth.domain.orders.event_type import EventType

event_type_bp = Blueprint('event_types', __name__, url_prefix='/event_types')
event_type_controller = EventTypeController()

@event_type_bp.get('')
def get_all_event_types() -> Response:
    return make_response(jsonify(event_type_controller.find_all()), HTTPStatus.OK)

@event_type_bp.post('')
def create_event_type() -> Response:
    content = request.get_json()
    event_type = EventType.create_from_dto(content)
    event_type_controller.create(event_type)
    return make_response(jsonify(event_type.put_into_dto()), HTTPStatus.CREATED)

@event_type_bp.get('/<int:type_id>')
def get_event_type(type_id: int) -> Response:
    return make_response(jsonify(event_type_controller.find_by_id(type_id)), HTTPStatus.OK)

@event_type_bp.put('/<int:type_id>')
def update_event_type(type_id: int) -> Response:
    content = request.get_json()
    event_type = EventType.create_from_dto(content)
    event_type_controller.update(type_id, event_type)
    return make_response("Event type updated", HTTPStatus.OK)

@event_type_bp.patch('/<int:type_id>')
def patch_event_type(type_id: int) -> Response:
    content = request.get_json()
    event_type_controller.patch(type_id, content)
    return make_response("Event type updated", HTTPStatus.OK)

@event_type_bp.delete('/<int:type_id>')
def delete_event_type(type_id: int) -> Response:
    event_type_controller.delete(type_id)
    return make_response("Event type deleted", HTTPStatus.OK)