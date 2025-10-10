from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from flasgger import swag_from
from my_project.auth.controller import newyear_controller
from my_project.auth.domain import NewYear
from my_project import db

newyear_bp = Blueprint('newyears', __name__, url_prefix='/api/newyears')

@newyear_bp.get('')
@swag_from({
    'tags': ['NewYear'],
    'summary': 'Get all New Year events',
    'responses': {200: {'description': 'List of New Year events'}}
})
def get_all_newyear() -> Response:
    result = db.session.execute("""
        SELECT id, event_date, duration, value
        FROM newyear
    """)
    newyears = [
        {"id": row[0], "event_date": str(row[1]), "duration": str(row[2]), "value": float(row[3])}
        for row in result.fetchall()
    ]
    return make_response(jsonify(newyears), HTTPStatus.OK)

@newyear_bp.post('')
@swag_from({
    'tags': ['NewYear'],
    'summary': 'Create New Year event',
    'parameters': [{
        'name': 'body',
        'in': 'body',
        'required': True,
        'schema': {
            'type': 'object',
            'properties': {
                'event_date': {'type': 'string', 'example': '2025-12-31'},
                'duration': {'type': 'string', 'example': '04:00:00'},
                'value': {'type': 'number', 'example': 1000.00}
            }
        }
    }],
    'responses': {201: {'description': 'Created'}}
})
def create_newyear() -> Response:
    content = request.get_json()
    newyear = NewYear.create_from_dto(content)
    newyear_controller.create(newyear)
    result = db.session.execute("""
        SELECT id, event_date, duration, value
        FROM newyear
        WHERE id = :id
    """, {'id': newyear.id})
    row = result.fetchone()
    newyear_dto = {"id": row[0], "event_date": str(row[1]), "duration": str(row[2]), "value": float(row[3])}
    return make_response(jsonify(newyear_dto), HTTPStatus.CREATED)

@newyear_bp.put('/<int:newyear_id>')
@swag_from({
    'tags': ['NewYear'],
    'summary': 'Update New Year event',
    'parameters': [
        {'name': 'newyear_id', 'in': 'path', 'type': 'integer', 'required': True},
        {'name': 'body', 'in': 'body', 'required': True, 'schema': {
            'type': 'object',
            'properties': {
                'event_date': {'type': 'string', 'example': '2025-12-31'},
                'duration': {'type': 'string', 'example': '04:00:00'},
                'value': {'type': 'number', 'example': 1000.00}
            }
        }}
    ],
    'responses': {200: {'description': 'Updated'}}
})
def update_newyear(newyear_id: int) -> Response:
    content = request.get_json()
    newyear = NewYear.create_from_dto(content)
    newyear_controller.update(newyear_id, newyear)
    return make_response("New Year event updated", HTTPStatus.OK)

@newyear_bp.delete('/<int:newyear_id>')
@swag_from({
    'tags': ['NewYear'],
    'summary': 'Delete New Year event',
    'parameters': [{'name': 'newyear_id', 'in': 'path', 'type': 'integer', 'required': True}],
    'responses': {200: {'description': 'Deleted'}}
})
def delete_newyear(newyear_id: int) -> Response:
    newyear_controller.delete(newyear_id)
    return make_response("New Year event deleted", HTTPStatus.OK)