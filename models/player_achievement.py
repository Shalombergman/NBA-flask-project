# from db import db
#
# class PlayerAchievement(db.Model):
#     __tablename__ = "player_achievements"
#     id = db.Column(db.Integer, primary_key=True)
#     player_id = db.Column(db.Integer, db.ForeignKey("players.id"))
#     achievement_id = db.Column(db.Integer, db.ForeignKey("achievements.id"))
#     count = db.Column(db.Integer, default=1)
#     player = db.relationship("Player", back_populates="player_achievements")
#     achievement = db.relationship("Achievement", back_populates="player_achievements")
#
#     def serialize(self):
#         return {
#             "id": self.id,
#             "player_id": self.player_id,
#             "achievement_id": self.achievement_id,
#             "count": self.count,
#             "player": self.player.serialize(),
#             "achievement": self.achievement.to_dict()
#         }