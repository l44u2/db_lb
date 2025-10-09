# speciality_route.py
from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller.orders.speciality_controller import SpecialityController
from my_project.auth.domain.orders.speciality import Speciality

speciality_bp = Blueprint('specialities', __name__, url_prefix='/specialities')
speciality_controller = SpecialityController()

@speciality_bp.get('')
def get_all_specialities() -> Response:
    return make_response(jsonify(speciality_controller.find_all()), HTTPStatus.OK)

@speciality_bp.post('')
def create_speciality() -> Response:
    content = request.get_json()
    speciality = Speciality.create_from_dto(content)
    speciality_controller.create(speciality)
    return make_response(jsonify(speciality.put_into_dto()), HTTPStatus.CREATED)

@speciality_bp.get('/<int:speciality_id>')
def get_speciality(speciality_id: int) -> Response:
    return make_response(jsonify(speciality_controller.find_by_id(speciality_id)), HTTPStatus.OK)

@speciality_bp.put('/<int:speciality_id>')
def update_speciality(speciality_id: int) -> Response:
    content = request.get_json()
    speciality = Speciality.create_from_dto(content)
    speciality_controller.update(speciality_id, speciality)
    return make_response("Speciality updated", HTTPStatus.OK)

@speciality_bp.patch('/<int:speciality_id>')
def patch_speciality(speciality_id: int) -> Response:
    content = request.get_json()
    speciality_controller.patch(speciality_id, content)
    return make_response("Speciality updated", HTTPStatus.OK)

@speciality_bp.delete('/<int:speciality_id>')
def delete_speciality(speciality_id: int) -> Response:
    speciality_controller.delete(speciality_id)
    return make_response("Speciality deleted", HTTPStatus.OK)