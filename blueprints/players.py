
from flask import Blueprint, jsonify, request
from services import player_service

players_bp = Blueprint('players', __name__)

@players_bp.route('/', methods=['GET'])
def get_players():

    position = request.args.get('position')
    season = request.args.get('season')
    players = player_service.sync_players_data()
    return jsonify(players), 200

@players_bp.route('/sync', methods=['POST'])
def sync_players():
    player_service.sync_players_data()
    return jsonify({"message": "Players data synced successfully"}), 200