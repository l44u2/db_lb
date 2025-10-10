from http import HTTPStatus
from flask import Blueprint, jsonify, Response, make_response
from flasgger import swag_from
from my_project.auth.controller.orders.event_newyear_controller import EventNewYearController
from my_project.auth.domain.orders.event_newyear import EventNewYear

event_newyear_bp = Blueprint('event_newyear', __name__, url_prefix='/event_newyear')
event_newyear_controller = EventNewYearController()

@event_newyear_bp.get('')
@swag_from({
    'tags': ['EventNewyear'],
    'summary': 'Get all Event-Newyear mappings',
    'responses': {200: {'description': 'List of all Event-Newyear mappings'}}
})
def get_all_event_newyear() -> Response:
    return make_response(jsonify(event_newyear_controller.find_all()), HTTPStatus.OK)