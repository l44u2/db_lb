from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from flasgger import swag_from
from my_project.auth.controller.orders.event_type_controller import EventTypeController
from my_project.auth.domain.orders.event_type import EventType
from my_project import db

event_type_bp = Blueprint('event_types', __name__, url_prefix='/api/event_types')
event_type_controller = EventTypeController()

@event_type_bp.get('')
@swag_from({
    'tags': ['EventType'],
    'summary': 'Get all event types',
    'responses': {200: {'description': 'List of event types'}}
})
def get_all_event_types() -> Response:
    result = db.session.execute("""
        SELECT id, `type` FROM `type`
    """)
    types = [
        {"id": row[0], "type": row[1]}
        for row in result.fetchall()
    ]
    return make_response(jsonify(types), HTTPStatus.OK)

@event_type_bp.post('')
@swag_from({
    'tags': ['EventType'],
    'summary': 'Create event type',
    'parameters': [{
        'name': 'body',
        'in': 'body',
        'required': True,
        'schema': {
            'type': 'object',
            'properties': {
                'type': {'type': 'string', 'example': 'Wedding'}
            }
        }
    }],
    'responses': {201: {'description': 'Created'}}
})
def create_event_type() -> Response:
    content = request.get_json()
    event_type = EventType.create_from_dto(content)
    event_type_controller.create(event_type)
    result = db.session.execute("""
        SELECT id, `type` FROM `type`
        WHERE id = :id
    """, {'id': event_type.id})
    row = result.fetchone()
    type_dto = {"id": row[0], "type": row[1]}
    return make_response(jsonify(type_dto), HTTPStatus.CREATED)

@event_type_bp.put('/<int:type_id>')
@swag_from({
    'tags': ['EventType'],
    'summary': 'Update event type',
    'parameters': [
        {'name': 'type_id', 'in': 'path', 'type': 'integer', 'required': True},
        {'name': 'body', 'in': 'body', 'required': True, 'schema': {
            'type': 'object',
            'properties': {
                'type': {'type': 'string', 'example': 'Wedding'}
            }
        }}
    ],
    'responses': {200: {'description': 'Updated'}}
})
def update_event_type(type_id: int) -> Response:
    content = request.get_json()
    event_type = EventType.create_from_dto(content)
    event_type_controller.update(type_id, event_type)
    return make_response("Event type updated", HTTPStatus.OK)

@event_type_bp.delete('/<int:type_id>')
@swag_from({
    'tags': ['EventType'],
    'summary': 'Delete event type',
    'parameters': [{'name': 'type_id', 'in': 'path', 'type': 'integer', 'required': True}],
    'responses': {200: {'description': 'Deleted'}}
})
def delete_event_type(type_id: int) -> Response:
    event_type_controller.delete(type_id)
    return make_response("Event type deleted", HTTPStatus.OK)