from flask import Flask
from blog.user.views import user
from blog.articles.views import article
from blog.auth.views import auth, login_manager
from blog.models.database import db
from blog import config
from blog.models.database import migrate


def crate_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(config.DevConfig)
    register_dop(app)
    register_blueprinnts(app)
    return app


def register_dop(app):
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db, compare_type=True)


def register_blueprinnts(app: Flask):
    app.register_blueprint(user, name="users")
    app.register_blueprint(article, name="articles")
    app.register_blueprint(auth)
