from db import db
from models.player import Player

from services.nba_api_service import get_players_from_nba_api, SEASONS


def get_players_from_db(position, season=None):

    positions = ['PF', 'SF', 'SG', 'PG']
    if position in positions and season in SEASONS:
        query = Player.query.filter_by(position=position, season=season).all()
    elif position in positions:
        query = Player.query.filter_by(position=position).all()
    else:
        return None


    result = [{'playerName': Player.playerName,
               'team': Player.team,
               'position': Player.position,
               'season': Player.season,
               'points': Player.points,
               'games': Player.games,
               'twoPercent': Player.twoPercent,
               'threePercent': Player.threePercent,
               'ATR': Player.ATR,
               'PPG Ratio': Player.PPG}
            for player in query]
    return result






def save_player_data(player_data, season):
    existing_player = Player.query.filter_by(playerId=player_data.get("playerId"), season=season).first()
    if not existing_player:
        player = Player(
            playerId=player_data.get("playerId"),
            playerName=player_data.get("playerName"),
            position=player_data.get("position"),
            age=player_data.get("age"),
            games=player_data.get("games"),
            gamesStarted=player_data.get("gamesStarted"),
            minutesPg=player_data.get("minutesPg"),
            fieldGoals=player_data.get("fieldGoals"),
            fieldAttempts=player_data.get("fieldAttempts"),
            fieldPercent=player_data.get("fieldPercent"),
            threeFg=player_data.get("threeFg"),
            threeAttempts=player_data.get("threeAttempts"),
            threePercent=player_data.get("threePercent"),
            twoFg=player_data.get("twoFg"),
            twoAttempts=player_data.get("twoAttempts"),
            twoPercent=player_data.get("twoPercent"),
            effectFgPercent=player_data.get("effectFgPercent"),
            ft=player_data.get("ft"),
            ftAttempts=player_data.get("ftAttempts"),
            ftPercent=player_data.get("ftPercent"),
            offensiveRb=player_data.get("offensiveRb"),
            defensiveRb=player_data.get("defensiveRb"),
            totalRb=player_data.get("totalRb"),
            assists=player_data.get("assists"),
            steals=player_data.get("steals"),
            blocks=player_data.get("blocks"),
            turnovers=player_data.get("turnovers"),
            personalFouls=player_data.get("personalFouls"),
            points=player_data.get("points"),
            rebounds=player_data.get("totalRb"),
            season=season,
            team = player_data.get("team"),

        )
        db.session.add(player)
        db.session.commit()
        print(f"Player {player.playerName} saved successfully.")
    else:
        print(f"Player {existing_player.playerName} already exists in season {season}.")

def main():
    # with app.app_context():

        for season in SEASONS:
            players_data = get_players_from_nba_api(season)
            if players_data:
                for player_data in players_data:
                    save_player_data(player_data, season)

if __name__ == "__main__":
    from app import app
    with app.app_context():
        main()
# def add_or_update_player(player_data):
#     player = Player.query.filter_by(id=player_data['id']).first()
#     if not player:
#         player = Player(id=player_data['id'], name=player_data['name'], team_id=player_data['team_id'])
#         db.session.add(player)
#     else:
#         player.name = player_data['name']
#         player.team_id = player_data['team_id']
#
#     db.session.commit()