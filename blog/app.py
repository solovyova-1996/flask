from flask import Flask
from blog.user.views import user
from blog.articles.views import article
from blog.auth.views import auth,login_manager
from blog.models.database import db



def crate_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object('config.DevConfig')
    db.init_app(app)
    login_manager.init_app(app)
    register_blueprinnts(app)
    return app


def register_blueprinnts(app: Flask):
    app.register_blueprint(user)
    app.register_blueprint(article)
    app.register_blueprint(auth)


