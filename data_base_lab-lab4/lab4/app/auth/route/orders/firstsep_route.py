# firstsep_route.py
from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import firstsep_controller
from my_project.auth.domain.orders.firstsep import FirstSep

firstsep_bp = Blueprint('firstseps', __name__, url_prefix='/firstseps')

@firstsep_bp.get('')
def get_all_firstseps() -> Response:
    return make_response(jsonify(firstsep_controller.find_all()), HTTPStatus.OK)

@firstsep_bp.post('')
def create_firstsep() -> Response:
    content = request.get_json()
    firstsep = Firstsep.create_from_dto(content)
    firstsep_controller.create(firstsep)
    return make_response(jsonify(firstsep.put_into_dto()), HTTPStatus.CREATED)

@firstsep_bp.get('/<int:firstsep_id>')
def get_firstsep(firstsep_id: int) -> Response:
    return make_response(jsonify(firstsep_controller.find_by_id(firstsep_id)), HTTPStatus.OK)

@firstsep_bp.put('/<int:firstsep_id>') 
def update_firstsep(firstsep_id: int) -> Response:
    content = request.get_json()
    firstsep = Firstsep.create_from_dto(content)
    firstsep_controller.update(firstsep_id, firstsep)
    return make_response("First September event updated", HTTPStatus.OK)

@firstsep_bp.patch('/<int:firstsep_id>')
def patch_firstsep(firstsep_id: int) -> Response:
    content = request.get_json()
    firstsep_controller.patch(firstsep_id, content)
    return make_response("First September event updated", HTTPStatus.OK)

@firstsep_bp.delete('/<int:firstsep_id>')
def delete_firstsep(firstsep_id: int) -> Response:
    firstsep_controller.delete(firstsep_id)
    return make_response("First September event deleted", HTTPStatus.OK)