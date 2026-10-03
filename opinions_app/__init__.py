from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from opinions_app.settings import Config

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app)

    from opinions_app import error_handlers, models  # noqa
    from opinions_app.views import main_blueprint

    app.register_blueprint(main_blueprint)

    return app