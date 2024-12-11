from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import agency_controller
from my_project.auth.domain import Agency

agency_bp = Blueprint('agencies', __name__, url_prefix='/agencies')

@agency_bp.get('')
def get_all_agencies() -> Response:
    return make_response(jsonify(agency_controller.find_all()), HTTPStatus.OK)

@agency_bp.post('')
def create_agency() -> Response:
    content = request.get_json()
    agency = Agency.create_from_dto(content)
    agency_controller.create(agency)
    return make_response(jsonify(agency.put_into_dto()), HTTPStatus.CREATED)

@agency_bp.get('/<int:agency_id>')
def get_agency(agency_id: int) -> Response:
    return make_response(jsonify(agency_controller.find_by_id(agency_id)), HTTPStatus.OK)

@agency_bp.put('/<int:agency_id>')
def update_agency(agency_id: int) -> Response:
    content = request.get_json()
    agency = Agency.create_from_dto(content)
    agency_controller.update(agency_id, agency)
    return make_response("Agency updated", HTTPStatus.OK)

@agency_bp.patch('/<int:agency_id>')
def patch_agency(agency_id: int) -> Response:
    content = request.get_json()
    agency_controller.patch(agency_id, content)
    return make_response("Agency updated", HTTPStatus.OK)

@agency_bp.delete('/<int:agency_id>')
def delete_agency(agency_id: int) -> Response:
    agency_controller.delete(agency_id)
    return make_response("Agency deleted", HTTPStatus.OK)

@agency_bp.get('/get-agency-by-speciality/<int:speciality_id>')
def get_agency_by_speciality(speciality_id: int) -> Response:
    return make_response(jsonify(agency_controller.get_agency_by_speciality(speciality_id)),
                        HTTPStatus.OK)