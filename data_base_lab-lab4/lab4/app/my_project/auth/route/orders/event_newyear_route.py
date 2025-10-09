from http import HTTPStatus
from flask import Blueprint, jsonify, Response, make_response
from flasgger import swag_from
from my_project.auth.controller.orders.event_newyear_controller import EventNewYearController
from my_project.auth.domain.orders.event_newyear import EventNewYear

event_newyear_bp = Blueprint('event_newyear', __name__, url_prefix='/event_newyear')
event_newyear_controller = EventNewYearController()

@event_newyear_bp.get('')
@swag_from({
    'tags': ['EventNewyear'],
    'summary': 'Get all Event-Newyear mappings',
    'responses': {200: {'description': 'List of all Event-Newyear mappings'}}
})
def get_all_event_newyear() -> Response:
    return make_response(jsonify(event_newyear_controller.find_all()), HTTPStatus.OK)

@event_newyear_bp.get('/event/<int:event_id>')
@swag_from({
    'tags': ['EventNewyear'],
    'summary': 'Get Newyear mapping by Event ID',
    'parameters': [{'name': 'event_id', 'in': 'path', 'type': 'integer', 'required': True}],
    'responses': {200: {'description': 'List of Newyear IDs for the given Event'}}
})
def get_newyear_by_event(event_id: int) -> Response:
    return make_response(jsonify(event_newyear_controller.get_newyear_after_event(event_id)), HTTPStatus.OK)

@event_newyear_bp.get('/newyear/<int:newyear_id>')
@swag_from({
    'tags': ['EventNewyear'],
    'summary': 'Get Event mapping by Newyear ID',
    'parameters': [{'name': 'newyear_id', 'in': 'path', 'type': 'integer', 'required': True}],
    'responses': {200: {'description': 'List of Event IDs for the given Newyear'}}
})
def get_event_by_newyear(newyear_id: int) -> Response:
    return make_response(jsonify(event_newyear_controller.get_event_after_newyear(newyear_id)), HTTPStatus.OK)

@event_newyear_bp.delete('/<int:event_id>/<int:newyear_id>')
@swag_from({
    'tags': ['EventNewyear'],
    'summary': 'Delete Event-Newyear mapping',
    'parameters': [
        {'name': 'event_id', 'in': 'path', 'type': 'integer', 'required': True},
        {'name': 'newyear_id', 'in': 'path', 'type': 'integer', 'required': True}
    ],
    'responses': {200: {'description': 'Mapping deleted successfully'}}
})
def delete_event_newyear(event_id: int, newyear_id: int) -> Response:
    event_newyear_controller.delete_by_ids(event_id, newyear_id)
    return make_response("Event newyear mapping deleted", HTTPStatus.OK)