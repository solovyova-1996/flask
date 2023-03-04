from flask_login import UserMixin
from blog.models.database import db
from datetime import datetime


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    age = db.Column(db.Integer())
    password = db.Column(db.String(255))


class Article(db.Model):
    __tablename__ = 'articles'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    text = db.Column(db.Text())
    date = db.Column(db.Date(), default=datetime.now().date())
    author = db.Column(db.Integer(), db.ForeignKey("users.id", ondelete="cascade"), nullable=False)
