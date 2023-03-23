from flask_combo_jsonapi import ResourceList, ResourceDetail

from blog.permissions.user import UserPermission
from blog.shemas.shemas import UserShema
from blog.models.database import db
from blog.models.models import User, Article
from combojsonapi.event.resource import EventsResource


class UserDetailEvents(EventsResource):
    def event_get_article_count(self, **kwargs):
        return {'count': Article.query.filter(Article.author == kwargs["id"]).count()}


class UsersList(ResourceList):
    schema = UserShema
    data_layer = {
        'session': db.session,
        'model': User
    }


class UserDetail(ResourceDetail):
    events = UserDetailEvents
    schema = UserShema
    data_layer = {
        "permission_get": [UserPermission],
        'session': db.session,
        'model': User
    }
