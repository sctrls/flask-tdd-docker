import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from src.api.ping import ping_blueprint


# instantiate db
db = SQLAlchemy()

def create_app(script_info=None):
    app = Flask(__name__)

    # set configuration
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    # set up extension
    db.init_app(app)

    # register blueprints
    app.register_blueprint(ping_blueprint)

    # register app and db with the shell
    @app.shell_context_processor
    def ctx():
        return {'app': app, 'db': db}

    return app
