import json

from flask import Blueprint, jsonify

teams_bp = Blueprint('teams', __name__)

@teams_bp.route('/create', methods=['POST'])
def create_team(data):
    data = json.loads(data)
    return jsonify(data), 201