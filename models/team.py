from db import db

class Team(db.Model):
    __tablename__ = "fountain_teams"
    id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String, nullable=False)
    players_ids = db.Column(db.String, nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "team_name": self.team_name,
            "players_ids": self.players_ids
        }
