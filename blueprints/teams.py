import json

from flask import Blueprint, jsonify, request
from services import team_service

teams_bp = Blueprint('teams', __name__)

# @teams_bp.route('/create', methods=['POST'])
# def create_team(data):
#     data = json.loads(data)
#     return jsonify(data), 201


@teams_bp.route('/create', methods=['POST'])
def create_team():
    data = request.get_json()
    team = team_service.create_team(data['team_name'], data['player_ids'])
    return jsonify(team.to_dict()), 201

@teams_bp.route('/<int:team_id>', methods=['GET'])
def get_team(team_id):
    team = team_service.get_team(team_id)
    if team:
        return jsonify(team.to_dict()), 200
    return jsonify({"error": "Team not found"}), 404

@teams_bp.route('/<int:team_id>', methods=['PUT'])
def update_team(team_id):
    data = request.get_json()
    team = team_service.update_team(team_id, data.get('team_name'), data.get('player_ids'))
    if team:
        return jsonify(team.to_dict()), 200
    return jsonify({"error": "Team not found"}), 404

@teams_bp.route('/<int:team_id>', methods=['DELETE'])
def delete_team(team_id):
    if team_service.delete_team(team_id):
        return jsonify({"message": "Team deleted successfully"}), 200
    return jsonify({"error": "Team not found"}), 404

@teams_bp.route('/compare', methods=['POST'])
def compare_teams():
    data = request.get_json()
    team_ids = data.get('team_ids')
    if team_ids:
        teams = team_service.get_all_teams()
        # Implement comparison logic here
        return jsonify({"message": "Comparison not implemented yet"}), 501
    return jsonify({"error": "Missing team IDs"}), 400