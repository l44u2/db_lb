from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from flasgger import swag_from
from my_project.auth.controller import event_wedding_controller
from my_project.auth.domain import EventWedding
from my_project import db

event_wedding_bp = Blueprint('event_wedding', __name__, url_prefix='/api/event_wedding')

@event_wedding_bp.get('')
@swag_from({
    'tags': ['EventWedding'],
    'summary': 'Get all Event-Wedding mappings',
    'responses': {200: {'description': 'List of all Event-Wedding mappings'}}
})
def get_all_event_weddings() -> Response:
    result = db.session.execute("""
        SELECT event_id, wedding_id
        FROM event_wedding
    """)
    mappings = [
        {"event_id": row[0], "wedding_id": row[1]}
        for row in result.fetchall()
    ]
    return make_response(jsonify(mappings), HTTPStatus.OK)

@event_wedding_bp.get('/event/<int:event_id>')
@swag_from({
    'tags': ['EventWedding'],
    'summary': 'Get Wedding mapping by Event ID',
    'parameters': [{'name': 'event_id', 'in': 'path', 'type': 'integer', 'required': True}],
    'responses': {200: {'description': 'List of Wedding IDs for the given Event'}}
})
def get_wedding_by_event(event_id: int) -> Response:
    return make_response(jsonify(event_wedding_controller.get_wedding_by_event(event_id)), HTTPStatus.OK)

@event_wedding_bp.get('/wedding/<int:wedding_id>')
@swag_from({
    'tags': ['EventWedding'],
    'summary': 'Get Event mapping by Wedding ID',
    'parameters': [{'name': 'wedding_id', 'in': 'path', 'type': 'integer', 'required': True}],
    'responses': {200: {'description': 'List of Event IDs for the given Wedding'}}
})
def get_event_by_wedding(wedding_id: int) -> Response:
    return make_response(jsonify(event_wedding_controller.get_event_by_wedding(wedding_id)), HTTPStatus.OK)

@event_wedding_bp.delete('/<int:event_id>/<int:wedding_id>')
@swag_from({
    'tags': ['EventWedding'],
    'summary': 'Delete Event-Wedding mapping',
    'parameters': [
        {'name': 'event_id', 'in': 'path', 'type': 'integer', 'required': True},
        {'name': 'wedding_id', 'in': 'path', 'type': 'integer', 'required': True}
    ],
    'responses': {200: {'description': 'Mapping deleted successfully'}}
})
def delete_event_wedding(event_id: int, wedding_id: int) -> Response:
    event_wedding_controller.delete_by_ids(event_id, wedding_id)
    return make_response("Event wedding mapping deleted", HTTPStatus.OK)