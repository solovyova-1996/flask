from flask_combo_jsonapi import ResourceList, ResourceDetail
from blog.shemas.shemas import UserShema
from blog.models.database import db
from blog.models.models import User


class UsereList(ResourceList):
    schema = UserShema
    data_layer = {
        'session': db.session,
        'model': User
    }


class UserDetail(ResourceDetail):
    schema = UserShema
    data_layer = {
        'session': db.session,
        'model': User
    }
