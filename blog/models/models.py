from flask_login import UserMixin

from blog.models.database import db
from datetime import datetime

article_tag_association = db.Table('article_tag_association',
                                   db.Column("articles_id", db.Integer, db.ForeignKey("articles.id"), nullable=False,
                                             primary_key=True),
                                   db.Column("tags_id", db.Integer, db.ForeignKey("tags.id"), nullable=False,
                                             primary_key=True),
                                   )


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    age = db.Column(db.Integer())
    password = db.Column(db.String(255))


class Tag(db.Model):
    __tablename__ = 'tags'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, default='')
    articles = db.relationship("Article", secondary=article_tag_association, back_populates="tags", )


class Article(db.Model):
    __tablename__ = 'articles'
    id = db.Column(db.Integer, primary_key=True)
    tags = db.relationship("Tag", secondary=article_tag_association, back_populates="articles", )
    title = db.Column(db.String(255))
    text = db.Column(db.Text())
    date = db.Column(db.Date(), default=datetime.now().date())
    author = db.Column(db.Integer(), db.ForeignKey("users.id", ondelete="cascade"), nullable=False)
