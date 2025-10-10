from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from flasgger import swag_from
from my_project.auth.controller import event_controller
from my_project.auth.domain import Event

event_bp = Blueprint('events', __name__, url_prefix='/api/events')

@event_bp.get('')
@swag_from({
    'tags': ['Event'],
    'summary': 'Get all events',
    'responses': {200: {'description': 'List of events'}}
})
def get_all_events() -> Response:
    return make_response(jsonify(event_controller.find_all()), HTTPStatus.OK)

@event_bp.post('')
@swag_from({
    'tags': ['Event'],
    'summary': 'Create event',
    'parameters': [{
        'name': 'body',
        'in': 'body',
        'required': True,
        'schema': {
            'type': 'object',
            'properties': {
                'animator_id': {'type': 'integer', 'example': 1},
                'agency_id': {'type': 'integer', 'example': 1},
                'location_id': {'type': 'integer', 'example': 1},
                'type_id': {'type': 'integer', 'example': 1}
            }
        }
    }],
    'responses': {201: {'description': 'Created'}}
})
def create_event() -> Response:
    content = request.get_json()
    event = Event.create_from_dto(content)
    event_controller.create(event)
    return make_response(jsonify(event.put_into_dto()), HTTPStatus.CREATED)

@event_bp.put('/<int:event_id>')
@swag_from({
    'tags': ['Event'],
    'summary': 'Update event',
    'parameters': [
        {'name': 'event_id', 'in': 'path', 'type': 'integer', 'required': True},
        {'name': 'body', 'in': 'body', 'required': True, 'schema': {
            'type': 'object',
            'properties': {
                'animator_id': {'type': 'integer', 'example': 1},
                'agency_id': {'type': 'integer', 'example': 1},
                'location_id': {'type': 'integer', 'example': 1},
                'type_id': {'type': 'integer', 'example': 1}
            }
        }}
    ],
    'responses': {200: {'description': 'Updated'}}
})
def update_event(event_id: int) -> Response:
    content = request.get_json()
    event = Event.create_from_dto(content)
    event_controller.update(event_id, event)
    return make_response("Event updated", HTTPStatus.OK)

@event_bp.delete('/<int:event_id>')
@swag_from({
    'tags': ['Event'],
    'summary': 'Delete event',
    'parameters': [{'name': 'event_id', 'in': 'path', 'type': 'integer', 'required': True}],
    'responses': {200: {'description': 'Deleted'}}
})
def delete_event(event_id: int) -> Response:
    event_controller.delete(event_id)
    return make_response("Event deleted", HTTPStatus.OK)