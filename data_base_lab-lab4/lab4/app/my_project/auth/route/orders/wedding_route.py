from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from flasgger import swag_from
from my_project.auth.controller import wedding_controller
from my_project.auth.domain import Wedding
from my_project import db

wedding_bp = Blueprint('weddings', __name__, url_prefix='/api/weddings')

@wedding_bp.get('')
@swag_from({
    'tags': ['Wedding'],
    'summary': 'Get all weddings',
    'responses': {200: {'description': 'List of weddings'}}
})
def get_all_weddings() -> Response:
    result = db.session.execute("""
        SELECT id, event_date, duration, value
        FROM wedding
    """)
    weddings = [
        {"id": row[0], "event_date": str(row[1]), "duration": str(row[2]), "value": float(row[3])}
        for row in result.fetchall()
    ]
    return make_response(jsonify(weddings), HTTPStatus.OK)

@wedding_bp.post('')
@swag_from({
    'tags': ['Wedding'],
    'summary': 'Create wedding',
    'parameters': [{
        'name': 'body',
        'in': 'body',
        'required': True,
        'schema': {
            'type': 'object',
            'properties': {
                'event_date': {'type': 'string', 'example': '2025-07-20'},
                'duration': {'type': 'string', 'example': '05:00:00'},
                'value': {'type': 'number', 'example': 2000.00}
            }
        }
    }],
    'responses': {201: {'description': 'Created'}}
})
def create_wedding() -> Response:
    content = request.get_json()
    wedding = Wedding.create_from_dto(content)
    wedding_controller.create(wedding)
    result = db.session.execute("""
        SELECT id, event_date, duration, value
        FROM wedding
        WHERE id = :id
    """, {'id': wedding.id})
    row = result.fetchone()
    wedding_dto = {"id": row[0], "event_date": str(row[1]), "duration": str(row[2]), "value": float(row[3])}
    return make_response(jsonify(wedding_dto), HTTPStatus.CREATED)

@wedding_bp.get('/<int:wedding_id>')
@swag_from({
    'tags': ['Wedding'],
    'summary': 'Get wedding by ID',
    'parameters': [{'name': 'wedding_id', 'in': 'path', 'type': 'integer', 'required': True}],
    'responses': {200: {'description': 'Wedding'}, 404: {'description': 'Not found'}}
})
def get_wedding(wedding_id: int) -> Response:
    result = db.session.execute("""
        SELECT id, event_date, duration, value
        FROM wedding
        WHERE id = :id
    """, {'id': wedding_id})
    row = result.fetchone()
    if row is None:
        return make_response("Not found", HTTPStatus.NOT_FOUND)
    wedding = {"id": row[0], "event_date": str(row[1]), "duration": str(row[2]), "value": float(row[3])}
    return make_response(jsonify(wedding), HTTPStatus.OK)

@wedding_bp.put('/<int:wedding_id>')
@swag_from({
    'tags': ['Wedding'],
    'summary': 'Update wedding',
    'parameters': [
        {'name': 'wedding_id', 'in': 'path', 'type': 'integer', 'required': True},
        {'name': 'body', 'in': 'body', 'required': True, 'schema': {
            'type': 'object',
            'properties': {
                'event_date': {'type': 'string', 'example': '2025-07-20'},
                'duration': {'type': 'string', 'example': '05:00:00'},
                'value': {'type': 'number', 'example': 2000.00}
            }
        }}
    ],
    'responses': {200: {'description': 'Updated'}}
})
def update_wedding(wedding_id: int) -> Response:
    content = request.get_json()
    wedding = Wedding.create_from_dto(content)
    wedding_controller.update(wedding_id, wedding)
    return make_response("Wedding updated", HTTPStatus.OK)

@wedding_bp.patch('/<int:wedding_id>')
@swag_from({
    'tags': ['Wedding'],
    'summary': 'Partially update wedding',
    'parameters': [
        {'name': 'wedding_id', 'in': 'path', 'type': 'integer', 'required': True},
        {'name': 'body', 'in': 'body', 'required': True, 'schema': {
            'type': 'object',
            'properties': {
                'event_date': {'type': 'string', 'example': '2025-07-20'},
                'duration': {'type': 'string', 'example': '05:00:00'},
                'value': {'type': 'number', 'example': 2000.00}
            }
        }}
    ],
    'responses': {200: {'description': 'Updated'}}
})
def patch_wedding(wedding_id: int) -> Response:
    content = request.get_json()
    wedding_controller.patch(wedding_id, content)
    return make_response("Wedding updated", HTTPStatus.OK)

@wedding_bp.delete('/<int:wedding_id>')
@swag_from({
    'tags': ['Wedding'],
    'summary': 'Delete wedding',
    'parameters': [{'name': 'wedding_id', 'in': 'path', 'type': 'integer', 'required': True}],
    'responses': {200: {'description': 'Deleted'}}
})
def delete_wedding(wedding_id: int) -> Response:
    wedding_controller.delete(wedding_id)
    return make_response("Wedding deleted", HTTPStatus.OK)