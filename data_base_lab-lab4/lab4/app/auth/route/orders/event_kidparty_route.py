# event_kidparty_route.py
from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller.orders.event_kidparty_controller import EventKidPartyController
from my_project.auth.domain.orders.event_kidparty import EventKidParty

event_kidparty_bp = Blueprint('event_kidparties', __name__, url_prefix='/event_kidparties')
event_kidparty_controller = EventKidPartyController()

@event_kidparty_bp.get('')
def get_all_event_kidparties() -> Response:
    return make_response(jsonify(event_kidparty_controller.find_all()), HTTPStatus.OK)

@event_kidparty_bp.post('')
def create_event_kidparty() -> Response:
    content = request.get_json()
    event_kidparty = EventKidparty.create_from_dto(content)
    event_kidparty_controller.create(event_kidparty)
    return make_response(jsonify(event_kidparty.put_into_dto()), HTTPStatus.CREATED)

@event_kidparty_bp.get('/event/<int:event_id>')
def get_kidparty_by_event(event_id: int) -> Response:
    return make_response(jsonify(event_kidparty_controller.get_kidparty_after_event(event_id)), HTTPStatus.OK)

@event_kidparty_bp.get('/kidparty/<int:kidparty_id>')
def get_event_by_kidparty(kidparty_id: int) -> Response:
    return make_response(jsonify(event_kidparty_controller.get_event_after_kidparty(kidparty_id)), HTTPStatus.OK)

@event_kidparty_bp.delete('/<int:event_id>/<int:kidparty_id>')
def delete_event_kidparty(event_id: int, kidparty_id: int) -> Response:
    event_kidparty_controller.delete_by_ids(event_id, kidparty_id)
    return make_response("Event kidparty mapping deleted", HTTPStatus.OK)