from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from flasgger import swag_from
from my_project.auth.controller.orders.speciality_controller import SpecialityController
from my_project.auth.domain.orders.speciality import Speciality
from my_project import db

speciality_bp = Blueprint('specialities', __name__, url_prefix='/api/specialities')
speciality_controller = SpecialityController()

@speciality_bp.get('')
@swag_from({
    'tags': ['Speciality'],
    'summary': 'Get all specialities',
    'responses': {200: {'description': 'List of specialities'}}
})
def get_all_specialities() -> Response:
    result = db.session.execute("""
        SELECT id, speicality_type
        FROM speciality
    """)
    specialities = [
        {"id": row[0], "speciality_type": row[1]}
        for row in result.fetchall()
    ]
    return make_response(jsonify(specialities), HTTPStatus.OK)

@speciality_bp.post('')
@swag_from({
    'tags': ['Speciality'],
    'summary': 'Create speciality',
    'parameters': [{
        'name': 'body',
        'in': 'body',
        'required': True,
        'schema': {
            'type': 'object',
            'properties': {
                'speciality_type': {'type': 'string', 'example': 'Wedding Planning'}
            }
        }
    }],
    'responses': {201: {'description': 'Created'}}
})
def create_speciality() -> Response:
    content = request.get_json()
    speciality = Speciality.create_from_dto(content)
    speciality_controller.create(speciality)
    result = db.session.execute("""
        SELECT id, speicality_type
        FROM speciality
        WHERE id = :id
    """, {'id': speciality.id})
    row = result.fetchone()
    speciality_dto = {"id": row[0], "speciality_type": row[1]}
    return make_response(jsonify(speciality_dto), HTTPStatus.CREATED)

@speciality_bp.put('/<int:speciality_id>')
@swag_from({
    'tags': ['Speciality'],
    'summary': 'Update speciality',
    'parameters': [
        {'name': 'speciality_id', 'in': 'path', 'type': 'integer', 'required': True},
        {'name': 'body', 'in': 'body', 'required': True, 'schema': {
            'type': 'object',
            'properties': {
                'speciality_type': {'type': 'string', 'example': 'Wedding Planning'}
            }
        }}
    ],
    'responses': {200: {'description': 'Updated'}}
})
def update_speciality(speciality_id: int) -> Response:
    content = request.get_json()
    speciality = Speciality.create_from_dto(content)
    speciality_controller.update(speciality_id, speciality)
    return make_response("Speciality updated", HTTPStatus.OK)

@speciality_bp.delete('/<int:speciality_id>')
@swag_from({
    'tags': ['Speciality'],
    'summary': 'Delete speciality',
    'parameters': [{'name': 'speciality_id', 'in': 'path', 'type': 'integer', 'required': True}],
    'responses': {200: {'description': 'Deleted'}}
})
def delete_speciality(speciality_id: int) -> Response:
    speciality_controller.delete(speciality_id)
    return make_response("Speciality deleted", HTTPStatus.OK)