from flask import Flask


from blueprints.teams import teams_bp
from db import db

from flask_migrate import Migrate
from blueprints.players import players_bp


app = Flask(__name__)



app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nba.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.register_blueprint(players_bp, url_prefix='/players')
app.register_blueprint(teams_bp, url_prefix='/teams')


db.init_app(app)
migrate = Migrate(app, db)
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True,port=5002)