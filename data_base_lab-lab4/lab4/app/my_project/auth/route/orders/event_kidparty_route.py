from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from flasgger import swag_from
from my_project.auth.controller.orders.event_kidparty_controller import EventKidPartyController
from my_project.auth.domain.orders.event_kidparty import EventKidParty

event_kidparty_bp = Blueprint('event_kidparty', __name__, url_prefix='/event_kidparty')
event_kidparty_controller = EventKidPartyController()

@event_kidparty_bp.get('')
@swag_from({
    'tags': ['EventKidparty'],
    'summary': 'Get all Event-Kidparty mappings',
    'responses': {200: {'description': 'List of all Event-Kidparty mappings'}}
})
def get_all_event_kidparty() -> Response:
    return make_response(jsonify(event_kidparty_controller.find_all()), HTTPStatus.OK)