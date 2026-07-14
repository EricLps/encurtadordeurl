from flask import Flask
from .database import db
from .routes import bp
from flasgger import Swagger

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    Swagger(app)

    app.register_blueprint(bp)

    with app.app_context():
        db.create_all()

    return app