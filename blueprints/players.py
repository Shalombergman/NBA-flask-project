from flask import Blueprint, jsonify


from models.player import Player
from services import player_service




players_bp = Blueprint('players', __name__)


@players_bp.route('/players', methods=['GET'])
def get_players():
    players = Player.query.all()
    return jsonify([Player.to_dict(self=player) for player in players]), 200

@players_bp.route('/?position=<position>&season=>season>', methods=['GET'])
def get_position(position, season):
    return player_service.get_players_from_db(position, season)







# @players_bp.route('/players/create', methods=['POST'])
# def create_player():
#     data = request.get_json
#     # add_or_update_player(data)
#     return jsonify(data), 201
#
# @players_bp.route('/players/update', methods=['POST'])
# def update_players():
#     data = request.json
#     players = get_players_from_nba_api(data['team_id'])
#
#     for player in players:
#         # add_or_update_player(player)
#
#     return jsonify({"status": "success"}), 200