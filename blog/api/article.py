from flask_combo_jsonapi import ResourceList, ResourceDetail
from blog.shemas.shemas import ArticleShema
from blog.models.database import db
from blog.models.models import Article


class ArticleList(ResourceList):
    schema = ArticleShema
    data_layer = {
        'session': db.session,
        'model': Article
    }


class ArticleDetail(ResourceDetail):
    schema = ArticleShema
    data_layer = {
        'session': db.session,
        'model': Article
    }
