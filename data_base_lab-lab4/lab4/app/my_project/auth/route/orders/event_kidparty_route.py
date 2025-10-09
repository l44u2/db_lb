from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from flasgger import swag_from
from my_project.auth.controller.orders.event_kidparty_controller import EventKidPartyController
from my_project.auth.domain.orders.event_kidparty import EventKidParty

event_kidparty_bp = Blueprint('event_kidparty', __name__, url_prefix='/event_kidparty')
event_kidparty_controller = EventKidPartyController()

@event_kidparty_bp.get('')
@swag_from({
    'tags': ['EventKidparty'],
    'summary': 'Get all Event-Kidparty mappings',
    'responses': {200: {'description': 'List of all Event-Kidparty mappings'}}
})
def get_all_event_kidparty() -> Response:
    return make_response(jsonify(event_kidparty_controller.find_all()), HTTPStatus.OK)

@event_kidparty_bp.get('/event/<int:event_id>')
@swag_from({
    'tags': ['EventKidparty'],
    'summary': 'Get Kidparty mapping by Event ID',
    'parameters': [{'name': 'event_id', 'in': 'path', 'type': 'integer', 'required': True}],
    'responses': {200: {'description': 'List of Kidparty IDs for the given Event'}}
})
def get_kidparty_by_event(event_id: int) -> Response:
    return make_response(jsonify(event_kidparty_controller.get_kidparty_after_event(event_id)), HTTPStatus.OK)

@event_kidparty_bp.get('/kidparty/<int:kidparty_id>')
@swag_from({
    'tags': ['EventKidparty'],
    'summary': 'Get Event mapping by Kidparty ID',
    'parameters': [{'name': 'kidparty_id', 'in': 'path', 'type': 'integer', 'required': True}],
    'responses': {200: {'description': 'List of Event IDs for the given Kidparty'}}
})
def get_event_by_kidparty(kidparty_id: int) -> Response:
    return make_response(jsonify(event_kidparty_controller.get_event_after_kidparty(kidparty_id)), HTTPStatus.OK)

@event_kidparty_bp.delete('/<int:event_id>/<int:kidparty_id>')
@swag_from({
    'tags': ['EventKidparty'],
    'summary': 'Delete Event-Kidparty mapping',
    'parameters': [
        {'name': 'event_id', 'in': 'path', 'type': 'integer', 'required': True},
        {'name': 'kidparty_id', 'in': 'path', 'type': 'integer', 'required': True}
    ],
    'responses': {200: {'description': 'Mapping deleted successfully'}}
})
def delete_event_kidparty(event_id: int, kidparty_id: int) -> Response:
    event_kidparty_controller.delete_by_ids(event_id, kidparty_id)
    return make_response("Event kidparty mapping deleted", HTTPStatus.OK)