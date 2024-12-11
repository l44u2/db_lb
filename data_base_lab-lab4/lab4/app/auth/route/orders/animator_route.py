from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller.orders.animator_controller import AnimatorController
from my_project.auth.domain.orders.animator import Animator

animator_bp = Blueprint('animators', __name__, url_prefix='/animators')

# Create an instance of AnimatorController
animator_controller = AnimatorController()

@animator_bp.get('')
def get_all_animators() -> Response:
    return make_response(jsonify(animator_controller.find_all()), HTTPStatus.OK)

@animator_bp.post('')
def create_animator() -> Response:
    content = request.get_json()
    animator = Animator.create_from_dto(content)
    animator_controller.create(animator)
    return make_response(jsonify(animator.put_into_dto()), HTTPStatus.CREATED)

@animator_bp.get('/<int:animator_id>')
def get_animator(animator_id: int) -> Response:
    return make_response(jsonify(animator_controller.find_by_id(animator_id)), HTTPStatus.OK)

@animator_bp.put('/<int:animator_id>')
def update_animator(animator_id: int) -> Response:
    content = request.get_json()
    animator = Animator.create_from_dto(content)
    animator_controller.update(animator_id, animator)
    return make_response("Animator updated", HTTPStatus.OK)

@animator_bp.patch('/<int:animator_id>')
def patch_animator(animator_id: int) -> Response:
    content = request.get_json()
    animator_controller.patch(animator_id, content)
    return make_response("Animator updated", HTTPStatus.OK)

@animator_bp.delete('/<int:animator_id>')
def delete_animator(animator_id: int) -> Response:
    animator_controller.delete(animator_id)
    return make_response("Animator deleted", HTTPStatus.OK)