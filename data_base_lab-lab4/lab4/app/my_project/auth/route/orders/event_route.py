from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import event_controller
from my_project.auth.domain import Event

event_bp = Blueprint('events', __name__, url_prefix='/events')

@event_bp.get('')
def get_all_events() -> Response:
    return make_response(jsonify(event_controller.find_all()), HTTPStatus.OK)

@event_bp.post('')
def create_event() -> Response:
    content = request.get_json()
    event = Event.create_from_dto(content)
    event_controller.create(event)
    return make_response(jsonify(event.put_into_dto()), HTTPStatus.CREATED)

@event_bp.get('/<int:event_id>')
def get_event(event_id: int) -> Response:
    return make_response(jsonify(event_controller.find_by_id(event_id)), HTTPStatus.OK)

@event_bp.put('/<int:event_id>')
def update_event(event_id: int) -> Response:
    content = request.get_json()
    event = Event.create_from_dto(content)
    event_controller.update(event_id, event)
    return make_response("Event updated", HTTPStatus.OK)

@event_bp.patch('/<int:event_id>')
def patch_event(event_id: int) -> Response:
    content = request.get_json()
    event_controller.patch(event_id, content)
    return make_response("Event updated", HTTPStatus.OK)

@event_bp.delete('/<int:event_id>')
def delete_event(event_id: int) -> Response:
    event_controller.delete(event_id)
    return make_response("Event deleted", HTTPStatus.OK)

@event_bp.get('/get-events-by-animator/<int:animator_id>')
def get_events_by_animator(animator_id: int) -> Response:
    return make_response(jsonify(event_controller.get_events_by_animator(animator_id)),
                        HTTPStatus.OK)

@event_bp.get('/get-events-by-agency/<int:agency_id>')
def get_events_by_agency(agency_id: int) -> Response:
    return make_response(jsonify(event_controller.get_events_by_agency(agency_id)),
                        HTTPStatus.OK)

@event_bp.get('/get-events-by-location/<int:location_id>')
def get_events_by_location(location_id: int) -> Response:
    return make_response(jsonify(event_controller.get_events_by_location(location_id)),
                        HTTPStatus.OK)

@event_bp.get('/get-events-by-type/<int:type_id>')
def get_events_by_type(type_id: int) -> Response:
    return make_response(jsonify(event_controller.get_events_by_type(type_id)),
                        HTTPStatus.OK)