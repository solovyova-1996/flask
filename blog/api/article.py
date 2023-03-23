from flask_combo_jsonapi import ResourceList, ResourceDetail
from blog.shemas.shemas import ArticleShema
from blog.models.database import db
from blog.models.models import Article
from combojsonapi.event.resource import EventsResource

class ArticleListEvents(EventsResource):
    def event_get_count(self):
        return {"count": Article.query.count()}


class ArticleList(ResourceList):
    events = ArticleListEvents
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
