# # create_app.py
# from flask import Flask
# from flask.cli import load_dotenv
# from flask_migrate import Migrate
# from db import db
# from blueprints.players import players_bp
# from blueprints.teams import teams_bp
# from blueprints.achievements import achievements_bp
#
# def create_app():
#     # Load environment variables
#     load_dotenv()
#
#     # Create Flask app
#     app = Flask(__name__)
#
#     # Configurations
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nba.db'
#     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#
#     # Initialize database and migrations
#     db.init_app(app)
#     migrate = Migrate(app, db)
#
#     # Register blueprints
#     app.register_blueprint(players_bp, url_prefix='/players')
#     app.register_blueprint(teams_bp, url_prefix='/teams')
#     app.register_blueprint(achievements_bp, url_prefix='/achievements')
#
#     # Create tables
#     with app.app_context():
#         db.create_all()
#
#     return app