from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from flasgger import swag_from
from my_project.auth.controller import agency_controller
from my_project.auth.domain import Agency
from my_project import db

agency_bp = Blueprint('agencies', __name__, url_prefix='/api/agencies')

#@agency_bp.get('')
#@swag_from({
#    'tags': ['Agency'],
#    'summary': 'Get all agencies',
#    'responses': {200: {'description': 'List of agencies'}}
#})
def get_all_agencies() -> Response:
    result = db.session.execute("""
        SELECT agency.id, agency.name, agency.speciality_id, speciality.speicality_type
        FROM agency
        JOIN speciality ON agency.speciality_id = speciality.id
    """)
    agencies = [
        {"id": row[0], "name": row[1], "speciality_id": row[2], "speciality_type": row[3]}
        for row in result.fetchall()
    ]
    return make_response(jsonify(agencies), HTTPStatus.OK)

@agency_bp.post('')
@swag_from({
    'tags': ['Agency'],
    'summary': 'Create agency',
    'parameters': [{
        'name': 'body',
        'in': 'body',
        'required': True,
        'schema': {
            'type': 'object',
            'properties': {
                'name': {'type': 'string', 'example': 'Best Events Agency'},
                'speciality_id': {'type': 'integer', 'example': 1}
            }
        }
    }],
    'responses': {201: {'description': 'Created'}}
})
def create_agency() -> Response:
    content = request.get_json()
    agency = Agency.create_from_dto(content)
    agency_controller.create(agency)
    
    result = db.session.execute("""
        SELECT agency.id, agency.name, agency.speciality_id, speciality.speicality_type
        FROM agency
        JOIN speciality ON agency.speciality_id = speciality.id
        WHERE agency.id = :id
    """, {'id': agency.id})
    row = result.fetchone()
    agency_dto = {"id": row[0], "name": row[1], "speciality_id": row[2], "speciality_type": row[3]}
    
    return make_response(jsonify(agency_dto), HTTPStatus.CREATED)

@agency_bp.put('/<int:agency_id>')
@swag_from({
    'tags': ['Agency'],
    'summary': 'Update agency',
    'parameters': [
        {'name': 'agency_id', 'in': 'path', 'type': 'integer', 'required': True},
        {'name': 'body', 'in': 'body', 'required': True, 'schema': {'type': 'object'}}
    ],
    'responses': {200: {'description': 'Updated'}}
})
def update_agency(agency_id: int) -> Response:
    content = request.get_json()
    agency = Agency.create_from_dto(content)
    agency_controller.update(agency_id, agency)
    return make_response("Agency updated", HTTPStatus.OK)

@agency_bp.delete('/<int:agency_id>')
@swag_from({
    'tags': ['Agency'],
    'summary': 'Delete agency',
    'parameters': [{'name': 'agency_id', 'in': 'path', 'type': 'integer', 'required': True}],
    'responses': {200: {'description': 'Deleted'}}
})
def delete_agency(agency_id: int) -> Response:
    agency_controller.delete(agency_id)
    return make_response("Agency deleted", HTTPStatus.OK)

