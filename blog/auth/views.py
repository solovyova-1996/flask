from flask import Blueprint, redirect, url_for, render_template, request
from flask_login import LoginManager, login_user, login_required, logout_user
from blog.models import User
from werkzeug.security import check_password_hash

auth = Blueprint('auth', __name__, static_folder="../static")
login_manager = LoginManager()
login_manager.login_view = 'auth.login'


@auth.route('/login/', methods=['GET', "POST"], endpoint='login')
def login():
    if request.method == 'GET':
        return render_template('auth/login.html')
    email = request.form.get('email')
    if not email:
        return render_template("auth/login.html", error="email not passed")
    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password, request.form.get('password')):
        return render_template("auth/login.html", error=f"no user {email!r} found")
    login_user(user)
    return redirect(url_for('user.user_list'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('user.user_list'))


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).one_or_none()


@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('auth.login'))


__all__ = ['login', 'logout', 'load_user', 'unauthorized']
