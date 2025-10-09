from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from flasgger import swag_from
from my_project.auth.controller.orders.event_christmass_controller import EventChristmasController
from my_project.auth.domain.orders.event_christmass import EventChristmass

event_christmass_bp = Blueprint('event_christmass', __name__, url_prefix='/event_christmass')
event_christmass_controller = EventChristmasController()

@event_christmass_bp.get('')
@swag_from({
    'tags': ['EventChristmass'],
    'summary': 'Get all Event-Christmas mappings',
    'responses': {200: {'description': 'List of all Event-Christmas mappings'}}
})
def get_all_event_christmass() -> Response:
    return make_response(jsonify(event_christmass_controller.find_all()), HTTPStatus.OK)

@event_christmass_bp.get('/event/<int:event_id>')
@swag_from({
    'tags': ['EventChristmass'],
    'summary': 'Get Christmas mapping by Event ID',
    'parameters': [{'name': 'event_id', 'in': 'path', 'type': 'integer', 'required': True}],
    'responses': {200: {'description': 'List of Christmas IDs for the given Event'}}
})
def get_christmass_by_event(event_id: int) -> Response:
    return make_response(jsonify(event_christmass_controller.get_christmass_after_event(event_id)), HTTPStatus.OK)

@event_christmass_bp.get('/christmass/<int:christmass_id>')
@swag_from({
    'tags': ['EventChristmass'],
    'summary': 'Get Event mapping by Christmas ID',
    'parameters': [{'name': 'christmass_id', 'in': 'path', 'type': 'integer', 'required': True}],
    'responses': {200: {'description': 'List of Event IDs for the given Christmas'}}
})
def get_event_by_christmass(christmass_id: int) -> Response:
    return make_response(jsonify(event_christmass_controller.get_event_after_christmass(christmass_id)), HTTPStatus.OK)

@event_christmass_bp.delete('/<int:event_id>/<int:christmass_id>')
@swag_from({
    'tags': ['EventChristmass'],
    'summary': 'Delete Event-Christmas mapping',
    'parameters': [
        {'name': 'event_id', 'in': 'path', 'type': 'integer', 'required': True},
        {'name': 'christmass_id', 'in': 'path', 'type': 'integer', 'required': True}
    ],
    'responses': {200: {'description': 'Mapping deleted successfully'}}
})
def delete_event_christmass(event_id: int, christmass_id: int) -> Response:
    event_christmass_controller.delete_by_ids(event_id, christmass_id)
    return make_response("Event christmass mapping deleted", HTTPStatus.OK)
