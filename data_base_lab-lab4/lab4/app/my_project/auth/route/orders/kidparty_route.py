from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import kidparty_controller
from my_project.auth.domain.orders.kidparty import KidParty

kidparty_bp = Blueprint('kidparties', __name__, url_prefix='/kidparties')

@kidparty_bp.get('')
def get_all_kidparties() -> Response:
    return make_response(jsonify(kidparty_controller.find_all()), HTTPStatus.OK)

@kidparty_bp.post('')
def create_kidparty() -> Response:
    content = request.get_json()
    kidparty = Kidparty.create_from_dto(content)
    kidparty_controller.create(kidparty)
    return make_response(jsonify(kidparty.put_into_dto()), HTTPStatus.CREATED)

@kidparty_bp.get('/<int:kidparty_id>')
def get_kidparty(kidparty_id: int) -> Response:
    return make_response(jsonify(kidparty_controller.find_by_id(kidparty_id)), HTTPStatus.OK)

@kidparty_bp.put('/<int:kidparty_id>')
def update_kidparty(kidparty_id: int) -> Response:
    content = request.get_json()
    kidparty = Kidparty.create_from_dto(content)
    kidparty_controller.update(kidparty_id, kidparty)
    return make_response("Kidparty updated", HTTPStatus.OK)

@kidparty_bp.patch('/<int:kidparty_id>')
def patch_kidparty(kidparty_id: int) -> Response:
    content = request.get_json()
    kidparty_controller.patch(kidparty_id, content)
    return make_response("Kidparty updated", HTTPStatus.OK)

@kidparty_bp.delete('/<int:kidparty_id>')
def delete_kidparty(kidparty_id: int) -> Response:
    kidparty_controller.delete(kidparty_id)
    return make_response("Kidparty deleted", HTTPStatus.OK)