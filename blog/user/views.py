from flask import Blueprint, render_template, redirect
from werkzeug.exceptions import NotFound
from blog.models import User,Article

user = Blueprint('user', __name__, url_prefix="/users", static_folder="../static")


@user.route('/')
def user_list():
    users = User.query.all()
    return render_template('users/list.html', users=users)


@user.route('/<int:pk>')
def get_user(pk: int):
    try:
        user=User.query.filter_by(id=pk).one_or_none()
        articles = Article.query.filter_by(author=user.id)
    except KeyError:
        # raise NotFound(f"User id {pk} not found")
        return redirect("/users/")
    return render_template('users/details.html', user=user,articles =articles)
