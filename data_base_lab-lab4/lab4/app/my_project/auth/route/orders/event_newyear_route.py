# event_newyear_route.py
from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller.orders.event_newyear_controller import EventNewYearController
from my_project.auth.domain.orders.event_newyear import EventNewYear

event_newyear_bp = Blueprint('event_newyears', __name__, url_prefix='/event_newyears')
event_newyear_controller = EventNewYearController()

@event_newyear_bp.get('')
def get_all_event_newyears() -> Response:
    return make_response(jsonify(event_newyear_controller.find_all()), HTTPStatus.OK)

@event_newyear_bp.post('')
def create_event_newyear() -> Response:
    content = request.get_json()
    event_newyear = EventNewyear.create_from_dto(content)
    event_newyear_controller.create(event_newyear)
    return make_response(jsonify(event_newyear.put_into_dto()), HTTPStatus.CREATED)

@event_newyear_bp.get('/event/<int:event_id>')
def get_newyear_by_event(event_id: int) -> Response:
    return make_response(jsonify(event_newyear_controller.get_newyear_after_event(event_id)), HTTPStatus.OK)

@event_newyear_bp.get('/newyear/<int:newyear_id>')
def get_event_by_newyear(newyear_id: int) -> Response:
    return make_response(jsonify(event_newyear_controller.get_event_after_newyear(newyear_id)), HTTPStatus.OK)

@event_newyear_bp.delete('/<int:event_id>/<int:newyear_id>')
def delete_event_newyear(event_id: int, newyear_id: int) -> Response:
    event_newyear_controller.delete_by_ids(event_id, newyear_id)
    return make_response("Event newyear mapping deleted", HTTPStatus.OK)