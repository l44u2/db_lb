from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from flasgger import swag_from
from my_project.auth.controller import animator_controller
from my_project.auth.domain import Animator

animator_bp = Blueprint('animators', __name__, url_prefix='/api/animators')

@animator_bp.get('')
@swag_from({
    'tags': ['Animator'],
    'summary': 'Get all animators',
    'responses': {200: {'description': 'List of animators'}}
})
def get_all_animators() -> Response:
    return make_response(jsonify(animator_controller.find_all()), HTTPStatus.OK)

@animator_bp.post('')
@swag_from({
    'tags': ['Animator'],
    'summary': 'Create animator',
    'parameters': [{
        'name': 'body',
        'in': 'body',
        'required': True,
        'schema': {
            'type': 'object',
            'properties': {
                'name': {'type': 'string', 'example': 'John'},
                'surname': {'type': 'string', 'example': 'Doe'}
            }
        }
    }],
    'responses': {201: {'description': 'Created'}}
})
def create_animator() -> Response:
    content = request.get_json()
    animator = Animator.create_from_dto(content)
    animator_controller.create(animator)
    return make_response(jsonify(animator.put_into_dto()), HTTPStatus.CREATED)

@animator_bp.put('/<int:animator_id>')
@swag_from({
    'tags': ['Animator'],
    'summary': 'Update animator',
    'parameters': [
        {'name': 'animator_id', 'in': 'path', 'type': 'integer', 'required': True},
        {'name': 'body', 'in': 'body', 'required': True, 'schema': {'type': 'object'}}
    ],
    'responses': {200: {'description': 'Updated'}}
})
def update_animator(animator_id: int) -> Response:
    content = request.get_json()
    animator = Animator.create_from_dto(content)
    animator_controller.update(animator_id, animator)
    return make_response("Animator updated", HTTPStatus.OK)

@animator_bp.delete('/<int:animator_id>')
@swag_from({
    'tags': ['Animator'],
    'summary': 'Delete animator',
    'parameters': [{'name': 'animator_id', 'in': 'path', 'type': 'integer', 'required': True}],
    'responses': {200: {'description': 'Deleted'}}
})
def delete_animator(animator_id: int) -> Response:
    animator_controller.delete(animator_id)
    return make_response("Animator deleted", HTTPStatus.OK)