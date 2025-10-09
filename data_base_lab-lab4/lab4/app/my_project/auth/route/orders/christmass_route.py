from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import christmass_controller
from my_project.auth.domain import Christmass

christmass_bp = Blueprint('christmass', __name__, url_prefix='/christmass')

@christmass_bp.get('')
def get_all_christmass() -> Response:
    return make_response(jsonify(christmass_controller.find_all()), HTTPStatus.OK)

@christmass_bp.post('')
def create_christmass() -> Response:
    content = request.get_json()
    christmass = Christmass.create_from_dto(content)
    christmass_controller.create(christmass)
    return make_response(jsonify(christmass.put_into_dto()), HTTPStatus.CREATED)

@christmass_bp.get('/<int:christmass_id>')
def get_christmass(christmass_id: int) -> Response:
    christmass = christmass_controller.find_by_id(christmass_id)
    return make_response(jsonify(christmass.put_into_dto()), HTTPStatus.OK)

@christmass_bp.put('/<int:christmass_id>')
def update_christmass(christmass_id: int) -> Response:
    content = request.get_json()
    christmass = Christmass.create_from_dto(content)
    christmass_controller.update(christmass_id, christmass)
    return make_response("Christmas event updated", HTTPStatus.OK)

@christmass_bp.patch('/<int:christmass_id>')
def patch_christmass(christmass_id: int) -> Response:
    content = request.get_json()
    christmass_controller.patch(christmass_id, content)
    return make_response("Christmas event updated", HTTPStatus.OK)

@christmass_bp.delete('/<int:christmass_id>')
def delete_christmass(christmass_id: int) -> Response:
    christmass_controller.delete(christmass_id)
    return make_response("Christmas event deleted", HTTPStatus.OK)