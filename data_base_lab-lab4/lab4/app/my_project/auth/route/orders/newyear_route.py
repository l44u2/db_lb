# newyear_route.py
from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import newyear_controller
from my_project.auth.domain import NewYear

newyear_bp = Blueprint('newyear', __name__, url_prefix='/newyear')

@newyear_bp.get('')
def get_all_newyear() -> Response:
    return make_response(jsonify(newyear_controller.find_all()), HTTPStatus.OK)

@newyear_bp.post('')
def create_newyear() -> Response:
    content = request.get_json()
    newyear = Newyear.create_from_dto(content)
    newyear_controller.create(newyear)
    return make_response(jsonify(newyear.put_into_dto()), HTTPStatus.CREATED)

@newyear_bp.get('/<int:newyear_id>')
def get_newyear(newyear_id: int) -> Response:
    return make_response(jsonify(newyear_controller.find_by_id(newyear_id)), HTTPStatus.OK)

@newyear_bp.put('/<int:newyear_id>')
def update_newyear(newyear_id: int) -> Response:
    content = request.get_json()
    newyear = Newyear.create_from_dto(content)
    newyear_controller.update(newyear_id, newyear)
    return make_response("New Year event updated", HTTPStatus.OK)

@newyear_bp.patch('/<int:newyear_id>')
def patch_newyear(newyear_id: int) -> Response:
    content = request.get_json()
    newyear_controller.patch(newyear_id, content)
    return make_response("New Year event updated", HTTPStatus.OK)

@newyear_bp.delete('/<int:newyear_id>')
def delete_newyear(newyear_id: int) -> Response:
    newyear_controller.delete(newyear_id)
    return make_response("New Year event deleted", HTTPStatus.OK)