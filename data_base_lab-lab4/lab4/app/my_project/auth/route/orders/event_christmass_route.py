from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from flasgger import swag_from
from my_project.auth.controller.orders.event_christmass_controller import EventChristmasController
from my_project.auth.domain.orders.event_christmass import EventChristmass

event_christmass_bp = Blueprint('event_christmass', __name__, url_prefix='/event_christmass')
event_christmass_controller = EventChristmasController()

@event_christmass_bp.get('')
@swag_from({
    'tags': ['EventChristmass'],
    'summary': 'Get all Event-Christmas mappings',
    'responses': {200: {'description': 'List of all Event-Christmas mappings'}}
})
def get_all_event_christmass() -> Response:
    return make_response(jsonify(event_christmass_controller.find_all()), HTTPStatus.OK)