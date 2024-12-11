# location_route.py
from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import location_controller
from my_project.auth.domain import Location

location_bp = Blueprint('locations', __name__, url_prefix='/locations')

@location_bp.get('')
def get_all_locations() -> Response:
    return make_response(jsonify(location_controller.find_all()), HTTPStatus.OK)

@location_bp.post('')
def create_location() -> Response:
    content = request.get_json()
    location = Location.create_from_dto(content)
    location_controller.create(location)
    return make_response(jsonify(location.put_into_dto()), HTTPStatus.CREATED)

@location_bp.get('/<int:location_id>')
def get_location(location_id: int) -> Response:
    return make_response(jsonify(location_controller.find_by_id(location_id)), HTTPStatus.OK)

@location_bp.put('/<int:location_id>')
def update_location(location_id: int) -> Response:
    content = request.get_json()
    location = Location.create_from_dto(content)
    location_controller.update(location_id, location)
    return make_response("Location updated", HTTPStatus.OK)

@location_bp.patch('/<int:location_id>')
def patch_location(location_id: int) -> Response:
    content = request.get_json()
    location_controller.patch(location_id, content)
    return make_response("Location updated", HTTPStatus.OK)

@location_bp.delete('/<int:location_id>')
def delete_location(location_id: int) -> Response:
    location_controller.delete(location_id)
    return make_response("Location deleted", HTTPStatus.OK)