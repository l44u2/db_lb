from http import HTTPStatus
from datetime import date, datetime, time
from typing import Any
from flask import Blueprint, jsonify, Response, request, make_response
from flasgger import swag_from
from my_project.auth.controller import birthday_controller
from my_project.auth.domain import Birthday
import dataclasses

birthday_bp = Blueprint('birthdays', __name__, url_prefix='/api/birthdays')


def _to_serializable(obj: Any) -> Any:

    if obj is None or isinstance(obj, (str, int, float, bool)):
        return obj

    if isinstance(obj, (datetime, date, time)):
        return obj.isoformat()

    if dataclasses.is_dataclass(obj):
        return _to_serializable(dataclasses.asdict(obj))

    if isinstance(obj, (list, tuple, set)):
        return [_to_serializable(v) for v in obj]

    if isinstance(obj, dict):
        return {str(k): _to_serializable(v) for k, v in obj.items()}

    if hasattr(obj, "put_into_dto") and callable(getattr(obj, "put_into_dto")):
        try:
            dto = obj.put_into_dto()
            return _to_serializable(dto)
        except Exception:
            pass

    if hasattr(obj, "__dict__"):
        return _to_serializable(vars(obj))

    return str(obj)


@birthday_bp.get('')
@swag_from({
    'tags': ['Birthday'],
    'summary': 'Get all birthdays',
    'responses': {200: {'description': 'List of birthdays'}}
})
def get_all_birthdays() -> Response:
    raw = birthday_controller.find_all()
    serializable = _to_serializable(raw)
    return make_response(jsonify(serializable), HTTPStatus.OK)


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
                'duration': {'type': 'string', 'example': '01:00:00'},
                'event_date': {'type': 'string', 'example': '2000-01-01'},
                'id': {'type': 'string', 'example': '6'},
                'value': {'type': 'string', 'example': '500'}
            }
        }
    }],
    'responses': {201: {'description': 'Created'}}
})
def create_birthday() -> Response:
    content = request.get_json()
    birthday = Birthday.create_from_dto(content)
    birthday_controller.create(birthday)
    return make_response(jsonify(_to_serializable(birthday.put_into_dto())), HTTPStatus.CREATED)


@birthday_bp.get('/<int:birthday_id>')
@swag_from({
    'tags': ['Birthday'],
    'summary': 'Get birthday by ID',
    'parameters': [{'name': 'birthday_id', 'in': 'path', 'type': 'integer', 'required': True}],
    'responses': {200: {'description': 'Birthday'}, 404: {'description': 'Not found'}}
})
def get_birthday(birthday_id: int) -> Response:
    raw = birthday_controller.find_by_id(birthday_id)
    return make_response(jsonify(_to_serializable(raw)), HTTPStatus.OK)


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
