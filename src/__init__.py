import os

from flask import Flask
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy
from werkzeug.middleware.proxy_fix import ProxyFix

# instantiate db
db = SQLAlchemy()
admin = Admin(template_mode="bootstrap3")


def create_app(script_info=None):
    app = Flask(__name__)
    app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_port=1)

    # set configuration
    app_settings = os.getenv("APP_SETTINGS")
    app.config.from_object(app_settings)

    # set up extensions: sqlalchemy and flask admin
    db.init_app(app)
    if os.getenv("FLASK_ENV") == "development":
        admin.init_app(app)

    # register flask RESTX api
    from src.api import api  # isort:skip

    api.init_app(app)

    # register app and db with the shell
    @app.shell_context_processor
    def ctx():
        return {"app": app, "db": db}

    return app
