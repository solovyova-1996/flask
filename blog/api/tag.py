from flask_combo_jsonapi import ResourceDetail, ResourceList
from blog.shemas import TagShema
from blog.models.database import db
from blog.models import Tag


class TagList(ResourceList):
    schema = TagShema
    data_layer = {
        'session': db.session,
        'model': Tag
    }


class TagDetail(ResourceDetail):
    schema = TagShema
    data_layer = {
        'session': db.session,
        'model': Tag
    }
