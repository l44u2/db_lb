from http import HTTPStatus
from flask import Blueprint, jsonify, Response, make_response
from flasgger import swag_from
from my_project.auth.controller.orders.event_firstsep_controller import EventFirstSepController
from my_project.auth.domain.orders.event_firstsep import EventFirstSep

event_firstsep_bp = Blueprint('event_firstsep', __name__, url_prefix='/event_firstsep')
event_firstsep_controller = EventFirstSepController()

@event_firstsep_bp.get('')
@swag_from({
    'tags': ['EventFirstsep'],
    'summary': 'Get all Event-Firstsep mappings',
    'responses': {200: {'description': 'List of all Event-Firstsep mappings'}}
})
def get_all_event_firstsep() -> Response:
    return make_response(jsonify(event_firstsep_controller.find_all()), HTTPStatus.OK)

@event_firstsep_bp.get('/event/<int:event_id>')
@swag_from({
    'tags': ['EventFirstsep'],
    'summary': 'Get Firstsep mapping by Event ID',
    'parameters': [{'name': 'event_id', 'in': 'path', 'type': 'integer', 'required': True}],
    'responses': {200: {'description': 'List of Firstsep IDs for the given Event'}}
})
def get_firstsep_by_event(event_id: int) -> Response:
    return make_response(jsonify(event_firstsep_controller.get_firstsep_after_event(event_id)), HTTPStatus.OK)

@event_firstsep_bp.get('/firstsep/<int:firstsep_id>')
@swag_from({
    'tags': ['EventFirstsep'],
    'summary': 'Get Event mapping by Firstsep ID',
    'parameters': [{'name': 'firstsep_id', 'in': 'path', 'type': 'integer', 'required': True}],
    'responses': {200: {'description': 'List of Event IDs for the given Firstsep'}}
})
def get_event_by_firstsep(firstsep_id: int) -> Response:
    return make_response(jsonify(event_firstsep_controller.get_event_after_firstsep(firstsep_id)), HTTPStatus.OK)

@event_firstsep_bp.delete('/<int:event_id>/<int:firstsep_id>')
@swag_from({
    'tags': ['EventFirstsep'],
    'summary': 'Delete Event-Firstsep mapping',
    'parameters': [
        {'name': 'event_id', 'in': 'path', 'type': 'integer', 'required': True},
        {'name': 'firstsep_id', 'in': 'path', 'type': 'integer', 'required': True}
    ],
    'responses': {200: {'description': 'Mapping deleted successfully'}}
})
def delete_event_firstsep(event_id: int, firstsep_id: int) -> Response:
    event_firstsep_controller.delete_by_ids(event_id, firstsep_id)
    return make_response("Event firstsep mapping deleted", HTTPStatus.OK)