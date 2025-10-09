from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from flasgger import swag_from
from my_project.auth.controller import firstsep_controller
from my_project.auth.domain.orders.firstsep import FirstSep
from my_project import db

firstsep_bp = Blueprint('firstseps', __name__, url_prefix='/api/firstseps')

@firstsep_bp.get('')
@swag_from({
    'tags': ['FirstSep'],
    'summary': 'Get all First September events',
    'responses': {200: {'description': 'List of First September events'}}
})
def get_all_firstseps() -> Response:
    result = db.session.execute("""
        SELECT id, event_date, duration, value
        FROM firstsep
    """)
    firstseps = [
        {"id": row[0], "event_date": str(row[1]), "duration": str(row[2]), "value": float(row[3])}
        for row in result.fetchall()
    ]
    return make_response(jsonify(firstseps), HTTPStatus.OK)

@firstsep_bp.post('')
@swag_from({
    'tags': ['FirstSep'],
    'summary': 'Create First September event',
    'parameters': [{
        'name': 'body',
        'in': 'body',
        'required': True,
        'schema': {
            'type': 'object',
            'properties': {
                'event_date': {'type': 'string', 'example': '2025-09-01'},
                'duration': {'type': 'string', 'example': '02:00:00'},
                'value': {'type': 'number', 'example': 500.00}
            }
        }
    }],
    'responses': {201: {'description': 'Created'}}
})
def create_firstsep() -> Response:
    content = request.get_json()
    firstsep = FirstSep.create_from_dto(content)
    firstsep_controller.create(firstsep)
    result = db.session.execute("""
        SELECT id, event_date, duration, value
        FROM firstsep
        WHERE id = :id
    """, {'id': firstsep.id})
    row = result.fetchone()
    firstsep_dto = {"id": row[0], "event_date": str(row[1]), "duration": str(row[2]), "value": float(row[3])}
    return make_response(jsonify(firstsep_dto), HTTPStatus.CREATED)

@firstsep_bp.get('/<int:firstsep_id>')
@swag_from({
    'tags': ['FirstSep'],
    'summary': 'Get First September event by ID',
    'parameters': [{'name': 'firstsep_id', 'in': 'path', 'type': 'integer', 'required': True}],
    'responses': {200: {'description': 'First September event'}, 404: {'description': 'Not found'}}
})
def get_firstsep(firstsep_id: int) -> Response:
    result = db.session.execute("""
        SELECT id, event_date, duration, value
        FROM firstsep
        WHERE id = :id
    """, {'id': firstsep_id})
    row = result.fetchone()
    if row is None:
        return make_response("Not found", HTTPStatus.NOT_FOUND)
    firstsep = {"id": row[0], "event_date": str(row[1]), "duration": str(row[2]), "value": float(row[3])}
    return make_response(jsonify(firstsep), HTTPStatus.OK)

@firstsep_bp.put('/<int:firstsep_id>')
@swag_from({
    'tags': ['FirstSep'],
    'summary': 'Update First September event',
    'parameters': [
        {'name': 'firstsep_id', 'in': 'path', 'type': 'integer', 'required': True},
        {'name': 'body', 'in': 'body', 'required': True, 'schema': {
            'type': 'object',
            'properties': {
                'event_date': {'type': 'string', 'example': '2025-09-01'},
                'duration': {'type': 'string', 'example': '02:00:00'},
                'value': {'type': 'number', 'example': 500.00}
            }
        }}
    ],
    'responses': {200: {'description': 'Updated'}}
})
def update_firstsep(firstsep_id: int) -> Response:
    content = request.get_json()
    firstsep = FirstSep.create_from_dto(content)
    firstsep_controller.update(firstsep_id, firstsep)
    return make_response("First September event updated", HTTPStatus.OK)

@firstsep_bp.patch('/<int:firstsep_id>')
@swag_from({
    'tags': ['FirstSep'],
    'summary': 'Partially update First September event',
    'parameters': [
        {'name': 'firstsep_id', 'in': 'path', 'type': 'integer', 'required': True},
        {'name': 'body', 'in': 'body', 'required': True, 'schema': {
            'type': 'object',
            'properties': {
                'event_date': {'type': 'string', 'example': '2025-09-01'},
                'duration': {'type': 'string', 'example': '02:00:00'},
                'value': {'type': 'number', 'example': 500.00}
            }
        }}
    ],
    'responses': {200: {'description': 'Updated'}}
})
def patch_firstsep(firstsep_id: int) -> Response:
    content = request.get_json()
    firstsep_controller.patch(firstsep_id, content)
    return make_response("First September event updated", HTTPStatus.OK)

@firstsep_bp.delete('/<int:firstsep_id>')
@swag_from({
    'tags': ['FirstSep'],
    'summary': 'Delete First September event',
    'parameters': [{'name': 'firstsep_id', 'in': 'path', 'type': 'integer', 'required': True}],
    'responses': {200: {'description': 'Deleted'}}
})
def delete_firstsep(firstsep_id: int) -> Response:
    firstsep_controller.delete(firstsep_id)
    return make_response("First September event deleted", HTTPStatus.OK)