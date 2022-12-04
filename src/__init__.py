import os

from flask import Flask
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy

# instantiate db
db = SQLAlchemy()
admin = Admin(template_mode="bootstrap3")


def create_app(script_info=None):
    app = Flask(__name__)

    # set configuration
    app_settings = os.getenv("APP_SETTINGS")
    app.config.from_object(app_settings)

    # set up extension
    db.init_app(app)
    if os.getenv("FLASK_ENV") == "development":
        admin.init_app(app)

    # register blueprints
    from src.api.ping import ping_blueprint

    app.register_blueprint(ping_blueprint)

    from src.api.users.views import users_blueprint

    app.register_blueprint(users_blueprint)

    # register app and db with the shell
    @app.shell_context_processor
    def ctx():
        return {"app": app, "db": db}

    return app
