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

@event_bp.get('/<int:event_id>')
@swag_from({
    'tags': ['Event'],
    'summary': 'Get event by ID',
    'parameters': [{'name': 'event_id', 'in': 'path', 'type': 'integer', 'required': True}],
    'responses': {200: {'description': 'Event'}, 404: {'description': 'Not found'}}
})
def get_event(event_id: int) -> Response:
    return make_response(jsonify(event_controller.find_by_id(event_id)), HTTPStatus.OK)

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

@event_bp.patch('/<int:event_id>')
@swag_from({
    'tags': ['Event'],
    'summary': 'Partially update event',
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
def patch_event(event_id: int) -> Response:
    content = request.get_json()
    event_controller.patch(event_id, content)
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

@event_bp.get('/get-events-by-animator/<int:animator_id>')
@swag_from({
    'tags': ['Event'],
    'summary': 'Get events by animator',
    'parameters': [{'name': 'animator_id', 'in': 'path', 'type': 'integer', 'required': True}],
    'responses': {200: {'description': 'Events for this animator'}}
})
def get_events_by_animator(animator_id: int) -> Response:
    return make_response(jsonify(event_controller.get_events_by_animator(animator_id)),
                        HTTPStatus.OK)

@event_bp.get('/get-events-by-agency/<int:agency_id>')
@swag_from({
    'tags': ['Event'],
    'summary': 'Get events by agency',
    'parameters': [{'name': 'agency_id', 'in': 'path', 'type': 'integer', 'required': True}],
    'responses': {200: {'description': 'Events for this agency'}}
})
def get_events_by_agency(agency_id: int) -> Response:
    return make_response(jsonify(event_controller.get_events_by_agency(agency_id)),
                        HTTPStatus.OK)

@event_bp.get('/get-events-by-location/<int:location_id>')
@swag_from({
    'tags': ['Event'],
    'summary': 'Get events by location',
    'parameters': [{'name': 'location_id', 'in': 'path', 'type': 'integer', 'required': True}],
    'responses': {200: {'description': 'Events at this location'}}
})
def get_events_by_location(location_id: int) -> Response:
    return make_response(jsonify(event_controller.get_events_by_location(location_id)),
                        HTTPStatus.OK)

@event_bp.get('/get-events-by-type/<int:type_id>')
@swag_from({
    'tags': ['Event'],
    'summary': 'Get events by type',
    'parameters': [{'name': 'type_id', 'in': 'path', 'type': 'integer', 'required': True}],
    'responses': {200: {'description': 'Events of this type'}}
})
def get_events_by_type(type_id: int) -> Response:
    return make_response(jsonify(event_controller.get_events_by_type(type_id)),
                        HTTPStatus.OK)