from flask import Blueprint, render_template
from blog.models import Article, User
from flask_login import login_required, current_user

article = Blueprint('article', __name__, url_prefix="/articles", static_folder="../static")


@article.route('/')
@login_required
def articles_list():
    articles = Article.query.all()
    return render_template("articles/list.html", articles=articles, user=current_user)


@article.route("<int:id>")
@login_required
def get_article(id: int):
    article = Article.query.filter_by(id=id).first()
    user = User.query.filter_by(id=article.author).first()
    return render_template("articles/details.html", article=article, user=user)
