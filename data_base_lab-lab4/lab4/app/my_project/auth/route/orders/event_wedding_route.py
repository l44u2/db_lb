# event_wedding_route.py
from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import event_wedding_controller
from my_project.auth.domain import EventWedding

event_wedding_bp = Blueprint('event_weddings', __name__, url_prefix='/event_weddings')

@event_wedding_bp.get('')
def get_all_event_weddings() -> Response:
    return make_response(jsonify(event_wedding_controller.find_all()), HTTPStatus.OK)

@event_wedding_bp.post('')
def create_event_wedding() -> Response:
    content = request.get_json()
    event_wedding = EventWedding.create_from_dto(content)
    event_wedding_controller.create(event_wedding)
    return make_response(jsonify(event_wedding.put_into_dto()), HTTPStatus.CREATED)

@event_wedding_bp.get('/event/<int:event_id>')
def get_wedding_by_event(event_id: int) -> Response:
    return make_response(jsonify(event_wedding_controller.get_wedding_by_event(event_id)), HTTPStatus.OK)

@event_wedding_bp.get('/wedding/<int:wedding_id>')
def get_event_by_wedding(wedding_id: int) -> Response:
    return make_response(jsonify(event_wedding_controller.get_event_by_wedding(wedding_id)), HTTPStatus.OK)

@event_wedding_bp.delete('/<int:event_id>/<int:wedding_id>')
def delete_event_wedding(event_id: int, wedding_id: int) -> Response:
    event_wedding_controller.delete_by_ids(event_id, wedding_id)
    return make_response("Event wedding mapping deleted", HTTPStatus.OK)