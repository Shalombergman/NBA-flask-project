# from db import db
#
# class Achievement(db.Model):
#     __tablename__ = "achievements"
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String)
#     player_achievements = db.relationship("PlayerAchievement", back_populates="achievement")
#
#     def serialize(self):
#         return {
#             "id": self.id,
#             "name": self.name,
#             "player_achievements": self.player_achievements
#         }
