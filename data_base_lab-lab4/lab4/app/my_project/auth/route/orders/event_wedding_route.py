from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from flasgger import swag_from
from my_project.auth.controller import event_wedding_controller
from my_project.auth.domain import EventWedding
from my_project import db

event_wedding_bp = Blueprint('event_wedding', __name__, url_prefix='/api/event_wedding')

@event_wedding_bp.get('')
@swag_from({
    'tags': ['EventWedding'],
    'summary': 'Get all Event-Wedding mappings',
    'responses': {200: {'description': 'List of all Event-Wedding mappings'}}
})
def get_all_event_weddings() -> Response:
    result = db.session.execute("""
        SELECT event_id, wedding_id
        FROM event_wedding
    """)
    mappings = [
        {"event_id": row[0], "wedding_id": row[1]}
        for row in result.fetchall()
    ]
    return make_response(jsonify(mappings), HTTPStatus.OK)