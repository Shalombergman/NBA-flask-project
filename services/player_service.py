import json

from flask import current_app

from db import db
from models.player import Player

from services.nba_api_service import get_players_from_nba_api, SEASONS
from utils.calculations import calculate_ppg_ratio, calculate_atr



def get_players_from_db(position, season=None):
    query = Player.query
    if position:
        query = query.filter_by(position=position)
    if season:
        query = query.filter_by(season=season)
    players = query.all()
    return [player.to_dict() for player in players]


def save_player_data(player_data, season):
        if isinstance(player_data, str):
            player_data = json.loads(player_data)
        print(f"Received data: {player_data}")
        player_id = player_data.get("playerId")
        if not player_id:
            print("Missing playerId in the data.")
            return None

        existing_player = Player.query.filter_by(playerId=player_data.get("playerId"), season=season).first()
        if not existing_player:
            player_data.pop('id', None)
            try:
                player = Player(**player_data)
                player.season = season
                db.session.add(player)
                db.session.commit()
                print(f"Player {player.playerName} saved successfully.")
                return player
            except Exception as e:
                print(f"Error saving player: {e}")
                return None
        else:
             print(f"Player {existing_player.playerName} already exists in season {season}.")
             return existing_player


def update_player_statistics(player):
    player.ATR = calculate_atr(player.assists, player.turnovers)
    player.PPG = calculate_ppg_ratio(player.points, player.games)
    db.session.commit()
    return player

def sync_players_data():
    with current_app.app_context():
        for season in SEASONS:
            players_data = get_players_from_nba_api(season)
            if players_data:
                for player_data in players_data:
                    player = save_player_data(player_data, season)
                    if player:
                        update_player_statistics(player)
