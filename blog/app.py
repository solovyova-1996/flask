from flask import Flask, Response, request
from blog.user.views import user
from blog.articles.views import article
def crate_app()->Flask:
    app = Flask(__name__)
    register_blueprinnts(app)
    return app

def register_blueprinnts(app:Flask):
    app.register_blueprint(user)
    app.register_blueprint(article)