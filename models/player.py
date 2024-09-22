from db import db


class Player(db.Model):
    __tablename__ = "players"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    playerId = db.Column(db.String, nullable=False)
    playerName = db.Column(db.String, nullable=False)
    position = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer)
    games = db.Column(db.Integer)
    gamesStarted = db.Column(db.Integer)
    minutesPg = db.Column(db.Integer)
    fieldGoals = db.Column(db.Integer)
    fieldAttempts = db.Column(db.Integer)
    fieldPercent = db.Column(db.Float)
    threeFg = db.Column(db.Integer)
    threeAttempts = db.Column(db.Integer)
    threePercent = db.Column(db.Float)
    twoFg = db.Column(db.Integer)
    twoAttempts = db.Column(db.Float)
    twoPercent = db.Column(db.Float)
    effectFgPercent = db.Column(db.Float)
    ft = db.Column(db.Integer)
    ftAttempts = db.Column(db.Integer)
    ftPercent = db.Column(db.Float)
    offensiveRb = db.Column(db.Integer)
    defensiveRb = db.Column(db.Integer)
    totalRb = db.Column(db.Integer)
    assists = db.Column(db.Integer)
    steals = db.Column(db.Integer)
    blocks = db.Column(db.Integer)
    turnovers = db.Column(db.Integer)
    personalFouls = db.Column(db.Integer)
    points = db.Column(db.Integer)
    rebounds = db.Column(db.Integer)
    season = db.Column(db.Integer, nullable=False)
    team = db.Column(db.String)
    ATR = db.Column(db.Float)
    PPG = db.Column(db.Float, default=0)



    def to_dict(self):
        return {
            "playerId": self.playerId,
            "playerName": self.playerName,
            "position": self.position,
            "age": self.age,
            "games": self.games,
            "gamesStarted": self.gamesStarted,
            "minutesPg": self.minutesPg,
            "fieldGoals": self.fieldGoals,
            "fieldAttempts": self.fieldAttempts,
            "fieldPercent": self.fieldPercent,
            "threeFg": self.threeFg,
            "threeAttempts": self.threeAttempts,
            "threePercent": self.threePercent,
            "twoFg": self.twoFg,
            "twoAttempts": self.twoAttempts,
            "twoPercent": self.twoPercent,
            "effectFgPercent": self.effectFgPercent,
            "ftPercent": self.ftPercent,
            "offensiveRb": self.offensiveRb,
            "defensiveRb": self.defensiveRb,
            "totalRb": self.totalRb,
            "assists": self.assists,
            "steals": self.steals,
            "blocks": self.blocks,
            "turnovers": self.turnovers,
            "personalFouls": self.personalFouls,
            "points": self.points,
            "rebounds": self.rebounds,
            "season": self.season,
            "team": self.team,
            "ATR": self.ATR,
            "PPG": self.PPG,
        }