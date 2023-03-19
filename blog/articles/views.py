from flask import Blueprint, render_template, request, current_app, redirect, url_for
from sqlalchemy.exc import IntegrityError

from blog.models import Article, User, Tag
from blog.models.database import db
from flask_login import login_required, current_user
from blog.forms import CreateArticleForm

article = Blueprint('art', __name__, url_prefix="/articles", static_folder="../static")


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


@article.route("/create/", methods=['POST', 'GET'], endpoint='create')
@login_required
def create_article():
    error = None
    form = CreateArticleForm(request.form)
    form.tags.choices = [(tag.id, tag.name) for tag in Tag.query.order_by("name")]
    if request.method == 'POST' and form.validate_on_submit():
        article = Article(title=form.title.data.strip(), text=form.text.data, author=current_user.id)
        if form.tags.data:
            selected_tags = Tag.query.filter(Tag.id.in_(form.tags.data))
            for tag in selected_tags:
                article.tags.append(tag)

        db.session.add(article)
        try:
            db.session.commit()
        except IntegrityError:
            current_app.logger.exception("Could not create a new article!")
            error = "Could not create article!"
        else:
            return redirect(url_for("articles.get_article", id=article.id))
    return render_template("articles/create.html", form=form, error=error)
