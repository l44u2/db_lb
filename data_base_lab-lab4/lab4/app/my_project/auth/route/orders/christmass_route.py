from http import HTTPStatus
from datetime import date, datetime, time
from typing import Any
from flask import Blueprint, jsonify, Response, request, make_response
from flasgger import swag_from
from my_project.auth.controller import christmass_controller
from my_project.auth.domain import Christmass
import dataclasses

christmass_bp = Blueprint('christmass', __name__, url_prefix='/api/christmass')


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


@christmass_bp.get('')
@swag_from({
    'tags': ['Christmass'],
    'summary': 'Get all Christmas events',
    'responses': {200: {'description': 'List of Christmas events'}}
})
def get_all_christmass() -> Response:
    raw = christmass_controller.find_all()
    serializable = _to_serializable(raw)
    return make_response(jsonify(serializable), HTTPStatus.OK)


@christmass_bp.post('')
@swag_from({
    'tags': ['Christmass'],
    'summary': 'Create Christmas event',
    'parameters': [{
        'name': 'body',
        'in': 'body',
        'required': True,
        'schema': {
            'type': 'object',
            'properties': {
                'event_date': {'type': 'string', 'format': 'date', 'example': '2024-12-25'},
                'duration': {'type': 'string', 'example': '03:00:00'},
                'value': {'type': 'number', 'example': 2000.00}
            }
        }
    }],
    'responses': {201: {'description': 'Created'}}
})
def create_christmass() -> Response:
    content = request.get_json()
    christmass = Christmass.create_from_dto(content)
    christmass_controller.create(christmass)
    return make_response(jsonify(_to_serializable(christmass.put_into_dto())), HTTPStatus.CREATED)


@christmass_bp.get('/<int:christmass_id>')
@swag_from({
    'tags': ['Christmass'],
    'summary': 'Get Christmas event by ID',
    'parameters': [{'name': 'christmass_id', 'in': 'path', 'type': 'integer', 'required': True}],
    'responses': {200: {'description': 'Christmas event'}, 404: {'description': 'Not found'}}
})
def get_christmass(christmass_id: int) -> Response:
    raw = christmass_controller.find_by_id(christmass_id)
    return make_response(jsonify(_to_serializable(raw)), HTTPStatus.OK)


@christmass_bp.put('/<int:christmass_id>')
@swag_from({
    'tags': ['Christmass'],
    'summary': 'Update Christmas event',
    'parameters': [
        {'name': 'christmass_id', 'in': 'path', 'type': 'integer', 'required': True},
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'event_date': {'type': 'string', 'format': 'date', 'example': '2024-12-25'},
                    'duration': {'type': 'string', 'example': '03:00:00'},
                    'value': {'type': 'number', 'example': 2000.00}
                }
            }
        }
    ],
    'responses': {200: {'description': 'Updated'}}
})
def update_christmass(christmass_id: int) -> Response:
    content = request.get_json()
    christmass = Christmass.create_from_dto(content)
    christmass_controller.update(christmass_id, christmass)
    return make_response("Christmas event updated", HTTPStatus.OK)


@christmass_bp.patch('/<int:christmass_id>')
@swag_from({
    'tags': ['Christmass'],
    'summary': 'Patch Christmas event (partial update)',
    'parameters': [
        {'name': 'christmass_id', 'in': 'path', 'type': 'integer', 'required': True},
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'event_date': {'type': 'string', 'format': 'date'},
                    'duration': {'type': 'string'},
                    'value': {'type': 'number'}
                }
            }
        }
    ],
    'responses': {200: {'description': 'Patched'}}
})
def patch_christmass(christmass_id: int) -> Response:
    content = request.get_json()
    christmass_controller.patch(christmass_id, content)
    return make_response("Christmas event updated", HTTPStatus.OK)


@christmass_bp.delete('/<int:christmass_id>')
@swag_from({
    'tags': ['Christmass'],
    'summary': 'Delete Christmas event',
    'parameters': [{'name': 'christmass_id', 'in': 'path', 'type': 'integer', 'required': True}],
    'responses': {200: {'description': 'Deleted'}}
})
def delete_christmass(christmass_id: int) -> Response:
    christmass_controller.delete(christmass_id)
    return make_response("Christmas event deleted", HTTPStatus.OK)