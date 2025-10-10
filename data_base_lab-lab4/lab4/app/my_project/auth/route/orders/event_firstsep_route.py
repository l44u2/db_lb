from http import HTTPStatus
from flask import Blueprint, jsonify, Response, make_response
from flasgger import swag_from
from my_project.auth.controller.orders.event_firstsep_controller import EventFirstSepController
from my_project.auth.domain.orders.event_firstsep import EventFirstSep

event_firstsep_bp = Blueprint('event_firstsep', __name__, url_prefix='/event_firstsep')
event_firstsep_controller = EventFirstSepController()

@event_firstsep_bp.get('')
@swag_from({
    'tags': ['EventFirstsep'],
    'summary': 'Get all Event-Firstsep mappings',
    'responses': {200: {'description': 'List of all Event-Firstsep mappings'}}
})
def get_all_event_firstsep() -> Response:
    return make_response(jsonify(event_firstsep_controller.find_all()), HTTPStatus.OK)