# event_christmass_route.py
from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller.orders.event_christmass_controller import EventChristmasController
from my_project.auth.domain.orders.event_christmass import EventChristmass

event_christmass_bp = Blueprint('event_christmass', __name__, url_prefix='/event_christmass')
event_christmass_controller = EventChristmasController()

@event_christmass_bp.get('')
def get_all_event_christmass() -> Response:
    return make_response(jsonify(event_christmass_controller.find_all()), HTTPStatus.OK)

@event_christmass_bp.post('')
def create_event_christmass() -> Response:
    content = request.get_json()
    event_christmass = EventChristmass.create_from_dto(content)
    event_christmass_controller.create(event_christmass)
    return make_response(jsonify(event_christmass.put_into_dto()), HTTPStatus.CREATED)

@event_christmass_bp.get('/event/<int:event_id>')
def get_christmass_by_event(event_id: int) -> Response:
    return make_response(jsonify(event_christmass_controller.get_christmass_after_event(event_id)), HTTPStatus.OK)

@event_christmass_bp.get('/christmass/<int:christmass_id>')
def get_event_by_christmass(christmass_id: int) -> Response:
    return make_response(jsonify(event_christmass_controller.get_event_after_christmass(christmass_id)), HTTPStatus.OK)

@event_christmass_bp.delete('/<int:event_id>/<int:christmass_id>')
def delete_event_christmass(event_id: int, christmass_id: int) -> Response:
    event_christmass_controller.delete_by_ids(event_id, christmass_id)
    return make_response("Event christmass mapping deleted", HTTPStatus.OK)