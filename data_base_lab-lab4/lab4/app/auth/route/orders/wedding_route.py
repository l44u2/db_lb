# wedding_route.py
from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import wedding_controller
from my_project.auth.domain import Wedding

wedding_bp = Blueprint('weddings', __name__, url_prefix='/weddings')

@wedding_bp.get('')
def get_all_weddings() -> Response:
    return make_response(jsonify(wedding_controller.find_all()), HTTPStatus.OK)

@wedding_bp.post('')
def create_wedding() -> Response:
    content = request.get_json()
    wedding = Wedding.create_from_dto(content)
    wedding_controller.create(wedding)
    return make_response(jsonify(wedding.put_into_dto()), HTTPStatus.CREATED)

@wedding_bp.get('/<int:wedding_id>')
def get_wedding(wedding_id: int) -> Response:
    return make_response(jsonify(wedding_controller.find_by_id(wedding_id)), HTTPStatus.OK)

@wedding_bp.put('/<int:wedding_id>')
def update_wedding(wedding_id: int) -> Response:
    content = request.get_json()
    wedding = Wedding.create_from_dto(content)
    wedding_controller.update(wedding_id, wedding)
    return make_response("Wedding updated", HTTPStatus.OK)

@wedding_bp.patch('/<int:wedding_id>')
def patch_wedding(wedding_id: int) -> Response:
    content = request.get_json()
    wedding_controller.patch(wedding_id, content)
    return make_response("Wedding updated", HTTPStatus.OK)

@wedding_bp.delete('/<int:wedding_id>')
def delete_wedding(wedding_id: int) -> Response:
    wedding_controller.delete(wedding_id)
    return make_response("Wedding deleted", HTTPStatus.OK)