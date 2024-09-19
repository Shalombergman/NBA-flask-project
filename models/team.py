from db import db

class Team(db.Model):
    __tablename__ = "fountain_teams"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    players = db.Column(db.String, nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "players": self.players
        }
