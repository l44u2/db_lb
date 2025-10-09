from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from flasgger import swag_from
from my_project.auth.controller import birthday_controller
from my_project.auth.domain import Birthday

birthday_bp = Blueprint('birthdays', __name__, url_prefix='/api/birthdays')

@birthday_bp.get('')
@swag_from({
    'tags': ['Birthday'],
    'summary': 'Get all birthdays',
    'responses': {200: {'description': 'List of birthdays'}}
})
def get_all_birthdays() -> Response:
    return make_response(jsonify(birthday_controller.find_all()), HTTPStatus.OK)

@birthday_bp.post('')
@swag_from({
    'tags': ['Birthday'],
    'summary': 'Create birthday',
    'parameters': [{
        'name': 'body',
        'in': 'body',
        'required': True,
        'schema': {
            'type': 'object',
            'properties': {
                'name': {'type': 'string', 'example': 'Alice'},
                'surname': {'type': 'string', 'example': 'Smith'},
                'date': {'type': 'string', 'example': '2000-01-01'}
            }
        }
    }],
    'responses': {201: {'description': 'Created'}}
})
def create_birthday() -> Response:
    content = request.get_json()
    birthday = Birthday.create_from_dto(content)
    birthday_controller.create(birthday)
    return make_response(jsonify(birthday.put_into_dto()), HTTPStatus.CREATED)

@birthday_bp.get('/<int:birthday_id>')
@swag_from({
    'tags': ['Birthday'],
    'summary': 'Get birthday by ID',
    'parameters': [{'name': 'birthday_id', 'in': 'path', 'type': 'integer', 'required': True}],
    'responses': {200: {'description': 'Birthday'}, 404: {'description': 'Not found'}}
})
def get_birthday(birthday_id: int) -> Response:
    return make_response(jsonify(birthday_controller.find_by_id(birthday_id)), HTTPStatus.OK)

@birthday_bp.put('/<int:birthday_id>')
@swag_from({
    'tags': ['Birthday'],
    'summary': 'Update birthday',
    'parameters': [
        {'name': 'birthday_id', 'in': 'path', 'type': 'integer', 'required': True},
        {'name': 'body', 'in': 'body', 'required': True, 'schema': {'type': 'object'}}
    ],
    'responses': {200: {'description': 'Updated'}}
})
def update_birthday(birthday_id: int) -> Response:
    content = request.get_json()
    birthday = Birthday.create_from_dto(content)
    birthday_controller.update(birthday_id, birthday)
    return make_response("Birthday updated", HTTPStatus.OK)

@birthday_bp.patch('/<int:birthday_id>')
@swag_from({
    'tags': ['Birthday'],
    'summary': 'Patch birthday (partial update)',
    'parameters': [
        {'name': 'birthday_id', 'in': 'path', 'type': 'integer', 'required': True},
        {'name': 'body', 'in': 'body', 'required': True, 'schema': {'type': 'object'}}
    ],
    'responses': {200: {'description': 'Patched'}}
})
def patch_birthday(birthday_id: int) -> Response:
    content = request.get_json()
    birthday_controller.patch(birthday_id, content)
    return make_response("Birthday updated", HTTPStatus.OK)

@birthday_bp.delete('/<int:birthday_id>')
@swag_from({
    'tags': ['Birthday'],
    'summary': 'Delete birthday',
    'parameters': [{'name': 'birthday_id', 'in': 'path', 'type': 'integer', 'required': True}],
    'responses': {200: {'description': 'Deleted'}}
})
def delete_birthday(birthday_id: int) -> Response:
    birthday_controller.delete(birthday_id)
    return make_response("Birthday deleted", HTTPStatus.OK)
