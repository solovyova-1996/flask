from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators, TextAreaField,SelectMultipleField


class CreateArticleForm(FlaskForm):
    title = StringField('Название статьи', [validators.DataRequired()])
    text = TextAreaField('Текст статьи', [validators.DataRequired()])
    tags = SelectMultipleField("Tags", coerce=int)
    submit = SubmitField("Сохранить")
