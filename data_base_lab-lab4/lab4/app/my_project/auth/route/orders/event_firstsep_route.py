# event_firstsep_route.py
from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller.orders.event_firstsep_controller import EventFirstSepController
from my_project.auth.domain.orders.event_firstsep import EventFirstSep

event_firstsep_bp = Blueprint('event_firstseps', __name__, url_prefix='/event_firstseps')
event_firstsep_controller = EventFirstSepController()

@event_firstsep_bp.get('')
def get_all_event_firstseps() -> Response:
    return make_response(jsonify(event_firstsep_controller.find_all()), HTTPStatus.OK)

@event_firstsep_bp.post('')
def create_event_firstsep() -> Response:
    content = request.get_json()
    event_firstsep = EventFirstsep.create_from_dto(content)
    event_firstsep_controller.create(event_firstsep)
    return make_response(jsonify(event_firstsep.put_into_dto()), HTTPStatus.CREATED)

@event_firstsep_bp.get('/event/<int:event_id>')
def get_firstsep_by_event(event_id: int) -> Response:
    return make_response(jsonify(event_firstsep_controller.get_firstsep_after_event(event_id)), HTTPStatus.OK)

@event_firstsep_bp.get('/firstsep/<int:firstsep_id>')
def get_event_by_firstsep(firstsep_id: int) -> Response:
    return make_response(jsonify(event_firstsep_controller.get_event_after_firstsep(firstsep_id)), HTTPStatus.OK)

@event_firstsep_bp.delete('/<int:event_id>/<int:firstsep_id>')
def delete_event_firstsep(event_id: int, firstsep_id: int) -> Response:
    event_firstsep_controller.delete_by_ids(event_id, firstsep_id)
    return make_response("Event firstsep mapping deleted", HTTPStatus.OK)