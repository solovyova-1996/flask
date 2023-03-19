from flask import Blueprint, redirect, url_for, render_template, request, current_app
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from blog.models import User
from blog.models.database import db
from werkzeug.security import check_password_hash, generate_password_hash
from blog.forms import UserRegisterForm, LoginForm
from sqlalchemy.exc import IntegrityError

auth = Blueprint('auth', __name__, static_folder="../static")
login_manager = LoginManager()
login_manager.login_view = 'auth.login'


@auth.route('/register/', methods=['GET', 'POST'], endpoint='register')
def register():
    if current_user.is_authenticated:
        return render_template('users/list.html')
    error = None
    form = UserRegisterForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        if User.query.filter_by(email=form.email.data).count():
            form.email.errors.append("Пользователь с таким логином уже существует")
            return render_template('auth/register.html', form=form)
        user = User(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            age=form.age.data,
            password=generate_password_hash(form.password.data)
        )
        db.session.add(user)

        try:
            db.session.commit()
        except IntegrityError:
            current_app.logger.error("не удалось сохранить пользователя")
            error = "не удалось сохранить пользователя"
        else:
            current_app.logger.info(f"Создан пользователь {user}")
            login_user(user)
            return redirect(url_for('us.user_list'))
    return render_template('auth/register.html', form=form, error=error)


@auth.route('/login/', methods=['GET', "POST"], endpoint='login')
def login():
    form = LoginForm(request.form)
    if request.method == 'GET':
        return render_template('auth/login.html', form=form)
    email = form.email.data
    if not email:
        return render_template("auth/login.html", error="email not passed", form=form)
    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password, form.password.data):
        return render_template("auth/login.html", form=form, error=f"no user {email!r} found")
    login_user(user)
    return redirect(url_for('us.user_list'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('us.user_list'))


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).one_or_none()


@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('auth.login'))


__all__ = ['login', 'logout', 'load_user', 'unauthorized', 'register']
