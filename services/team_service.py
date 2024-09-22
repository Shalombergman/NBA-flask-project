from db import db
import json

from models.team import Team


def create_team(team_name, player_ids):
    team = Team(team_name=team_name, players_ids=json.dumps(player_ids))
    db.session.add(team)
    db.session.commit()
    return team

def get_team(team_id):
    return Team.query.get(team_id)

def update_team(team_id, team_name=None, player_ids=None):
    team = Team.query.get(team_id)
    if team:
        if team_name:
            team.team_name = team_name
        if player_ids:
            team.players_ids = json.dumps(player_ids)
        db.session.commit()
    return team

def delete_team(team_id):
    team = Team.query.get(team_id)
    if team:
        db.session.delete(team)
        db.session.commit()
        return True
    return False

def get_all_teams():
    return Team.query.all()