# birthday_route.py
from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import birthday_controller
from my_project.auth.domain import Birthday

birthday_bp = Blueprint('birthdays', __name__, url_prefix='/birthdays')

@birthday_bp.get('')
def get_all_birthdays() -> Response:
    return make_response(jsonify(birthday_controller.find_all()), HTTPStatus.OK)

@birthday_bp.post('')
def create_birthday() -> Response:
    content = request.get_json()
    birthday = Birthday.create_from_dto(content)
    birthday_controller.create(birthday)
    return make_response(jsonify(birthday.put_into_dto()), HTTPStatus.CREATED)

@birthday_bp.get('/<int:birthday_id>')
def get_birthday(birthday_id: int) -> Response:
    return make_response(jsonify(birthday_controller.find_by_id(birthday_id)), HTTPStatus.OK)

@birthday_bp.put('/<int:birthday_id>')
def update_birthday(birthday_id: int) -> Response:
    content = request.get_json()
    birthday = Birthday.create_from_dto(content)
    birthday_controller.update(birthday_id, birthday)
    return make_response("Birthday updated", HTTPStatus.OK)

@birthday_bp.patch('/<int:birthday_id>')
def patch_birthday(birthday_id: int) -> Response:
    content = request.get_json()
    birthday_controller.patch(birthday_id, content)
    return make_response("Birthday updated", HTTPStatus.OK)

@birthday_bp.delete('/<int:birthday_id>')
def delete_birthday(birthday_id: int) -> Response:
    birthday_controller.delete(birthday_id)
    return make_response("Birthday deleted", HTTPStatus.OK)