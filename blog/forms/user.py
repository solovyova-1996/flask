from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, SubmitField, EmailField


class UserRegisterForm(FlaskForm):
    first_name = StringField("Имя")
    last_name = StringField("Фамилия")
    email = EmailField("Email", [validators.Email("Пользователь с таким email уже существует"),
                                 validators.DataRequired("Поле обязательно для заполнения")])
    age = StringField("Возраст")
    password = PasswordField("Пароль", [validators.DataRequired("Поле обязательно для заполнения"),
                                        validators.EqualTo("confirm_password", message="Пароли не совпадают")])
    confirm_password = PasswordField("Повторите пароль", [validators.DataRequired("Поле обязательно для заполнения")])
    submit = SubmitField("Зарегистрироваться")


class LoginForm(FlaskForm):
    email = StringField("email")
    password = PasswordField("Пароль", [validators.DataRequired("Поле обязательно для заполнения")])
    submit = SubmitField("Войти")
