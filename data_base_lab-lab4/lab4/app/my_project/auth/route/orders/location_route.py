from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from flasgger import swag_from
from my_project.auth.controller import location_controller
from my_project.auth.domain import Location
from my_project import db

location_bp = Blueprint('locations', __name__, url_prefix='/api/locations')

@location_bp.get('')
@swag_from({
    'tags': ['Location'],
    'summary': 'Get all locations',
    'responses': {200: {'description': 'List of locations'}}
})
def get_all_locations() -> Response:
    result = db.session.execute("""
        SELECT id, house, street
        FROM location
    """)
    locations = [
        {"id": row[0], "house": row[1], "street": row[2]}
        for row in result.fetchall()
    ]
    return make_response(jsonify(locations), HTTPStatus.OK)

@location_bp.post('')
@swag_from({
    'tags': ['Location'],
    'summary': 'Create location',
    'parameters': [{
        'name': 'body',
        'in': 'body',
        'required': True,
        'schema': {
            'type': 'object',
            'properties': {
                'house': {'type': 'string', 'example': '123'},
                'street': {'type': 'string', 'example': 'Main St'}
            }
        }
    }],
    'responses': {201: {'description': 'Created'}}
})
def create_location() -> Response:
    content = request.get_json()
    location = Location.create_from_dto(content)
    location_controller.create(location)
    result = db.session.execute("""
        SELECT id, house, street
        FROM location
        WHERE id = :id
    """, {'id': location.id})
    row = result.fetchone()
    location_dto = {"id": row[0], "house": row[1], "street": row[2]}
    return make_response(jsonify(location_dto), HTTPStatus.CREATED)

@location_bp.get('/<int:location_id>')
@swag_from({
    'tags': ['Location'],
    'summary': 'Get location by ID',
    'parameters': [{'name': 'location_id', 'in': 'path', 'type': 'integer', 'required': True}],
    'responses': {200: {'description': 'Location'}, 404: {'description': 'Not found'}}
})
def get_location(location_id: int) -> Response:
    result = db.session.execute("""
        SELECT id, house, street
        FROM location
        WHERE id = :id
    """, {'id': location_id})
    row = result.fetchone()
    if row is None:
        return make_response("Not found", HTTPStatus.NOT_FOUND)
    location = {"id": row[0], "house": row[1], "street": row[2]}
    return make_response(jsonify(location), HTTPStatus.OK)

@location_bp.put('/<int:location_id>')
@swag_from({
    'tags': ['Location'],
    'summary': 'Update location',
    'parameters': [
        {'name': 'location_id', 'in': 'path', 'type': 'integer', 'required': True},
        {'name': 'body', 'in': 'body', 'required': True, 'schema': {
            'type': 'object',
            'properties': {
                'house': {'type': 'string', 'example': '123'},
                'street': {'type': 'string', 'example': 'Main St'}
            }
        }}
    ],
    'responses': {200: {'description': 'Updated'}}
})
def update_location(location_id: int) -> Response:
    content = request.get_json()
    location = Location.create_from_dto(content)
    location_controller.update(location_id, location)
    return make_response("Location updated", HTTPStatus.OK)

@location_bp.patch('/<int:location_id>')
@swag_from({
    'tags': ['Location'],
    'summary': 'Partially update location',
    'parameters': [
        {'name': 'location_id', 'in': 'path', 'type': 'integer', 'required': True},
        {'name': 'body', 'in': 'body', 'required': True, 'schema': {
            'type': 'object',
            'properties': {
                'house': {'type': 'string', 'example': '123'},
                'street': {'type': 'string', 'example': 'Main St'}
            }
        }}
    ],
    'responses': {200: {'description': 'Updated'}}
})
def patch_location(location_id: int) -> Response:
    content = request.get_json()
    location_controller.patch(location_id, content)
    return make_response("Location updated", HTTPStatus.OK)

@location_bp.delete('/<int:location_id>')
@swag_from({
    'tags': ['Location'],
    'summary': 'Delete location',
    'parameters': [{'name': 'location_id', 'in': 'path', 'type': 'integer', 'required': True}],
    'responses': {200: {'description': 'Deleted'}}
})
def delete_location(location_id: int) -> Response:
    location_controller.delete(location_id)
    return make_response("Location deleted", HTTPStatus.OK)