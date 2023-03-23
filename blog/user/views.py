import requests
from flask import Blueprint, render_template, redirect
from werkzeug.exceptions import NotFound
from blog.models import User, Article

user = Blueprint('users', __name__, url_prefix="/users", static_folder="../static")
host = "127.0.0.1"
port = "5000"

@user.route('/')
def user_list():
    users = User.query.all()
    return render_template('users/list.html', users=users)


@user.route('/<int:pk>')
def get_user(pk: int):
    try:
        user = User.query.filter_by(id=pk).one_or_none()
        articles = Article.query.filter_by(author=user.id)
        response = requests.get(f"http://127.0.0.1:5000/api/users/{pk}/event_get_article_count/").json()
        try:
            count = response['count']
        except KeyError:
            count = 0
    except KeyError:
        return redirect("/users/")
    return render_template('users/details.html', user=user, articles=articles,count = count)
