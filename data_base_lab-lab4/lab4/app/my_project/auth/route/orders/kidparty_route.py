from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from flasgger import swag_from
from my_project.auth.controller import kidparty_controller
from my_project.auth.domain.orders.kidparty import KidParty
from my_project import db

kidparty_bp = Blueprint('kidparties', __name__, url_prefix='/api/kidparties')

@kidparty_bp.get('')
@swag_from({
    'tags': ['KidParty'],
    'summary': 'Get all kid parties',
    'responses': {200: {'description': 'List of kid parties'}}
})
def get_all_kidparties() -> Response:
    result = db.session.execute("""
        SELECT id, event_date, duration, value
        FROM kidparty
    """)
    kidparties = [
        {"id": row[0], "event_date": str(row[1]), "duration": str(row[2]), "value": float(row[3])}
        for row in result.fetchall()
    ]
    return make_response(jsonify(kidparties), HTTPStatus.OK)

@kidparty_bp.post('')
@swag_from({
    'tags': ['KidParty'],
    'summary': 'Create kid party',
    'parameters': [{
        'name': 'body',
        'in': 'body',
        'required': True,
        'schema': {
            'type': 'object',
            'properties': {
                'event_date': {'type': 'string', 'example': '2025-06-15'},
                'duration': {'type': 'string', 'example': '03:00:00'},
                'value': {'type': 'number', 'example': 300.00}
            }
        }
    }],
    'responses': {201: {'description': 'Created'}}
})
def create_kidparty() -> Response:
    content = request.get_json()
    kidparty = KidParty.create_from_dto(content)
    kidparty_controller.create(kidparty)
    result = db.session.execute("""
        SELECT id, event_date, duration, value
        FROM kidparty
        WHERE id = :id
    """, {'id': kidparty.id})
    row = result.fetchone()
    kidparty_dto = {"id": row[0], "event_date": str(row[1]), "duration": str(row[2]), "value": float(row[3])}
    return make_response(jsonify(kidparty_dto), HTTPStatus.CREATED)

@kidparty_bp.put('/<int:kidparty_id>')
@swag_from({
    'tags': ['KidParty'],
    'summary': 'Update kid party',
    'parameters': [
        {'name': 'kidparty_id', 'in': 'path', 'type': 'integer', 'required': True},
        {'name': 'body', 'in': 'body', 'required': True, 'schema': {
            'type': 'object',
            'properties': {
                'event_date': {'type': 'string', 'example': '2025-06-15'},
                'duration': {'type': 'string', 'example': '03:00:00'},
                'value': {'type': 'number', 'example': 300.00}
            }
        }}
    ],
    'responses': {200: {'description': 'Updated'}}
})
def update_kidparty(kidparty_id: int) -> Response:
    content = request.get_json()
    kidparty = KidParty.create_from_dto(content)
    kidparty_controller.update(kidparty_id, kidparty)
    return make_response("Kid party updated", HTTPStatus.OK)

@kidparty_bp.delete('/<int:kidparty_id>')
@swag_from({
    'tags': ['KidParty'],
    'summary': 'Delete kid party',
    'parameters': [{'name': 'kidparty_id', 'in': 'path', 'type': 'integer', 'required': True}],
    'responses': {200: {'description': 'Deleted'}}
})
def delete_kidparty(kidparty_id: int) -> Response:
    kidparty_controller.delete(kidparty_id)
    return make_response("Kid party deleted", HTTPStatus.OK)