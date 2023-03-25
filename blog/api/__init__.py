from flask import Blueprint
from flask_combo_jsonapi import Api
from combojsonapi.spec import ApiSpecPlugin
from combojsonapi.event import EventPlugin
from combojsonapi.permission import PermissionPlugin
from blog.api.tag import TagList, TagDetail
from blog.api.article import ArticleList, ArticleDetail
from blog.api.user import UsersList, UserDetail

blueprint = Blueprint("api", __name__, url_prefix="/api/v1")


def create_api_spec_plugin(app):
    api_spec_plugin = ApiSpecPlugin(
        app=app,
        tags={
            "Tag": "Tag API",
            "Article": "Article API",
            "User": "User API",
        }
    )
    return api_spec_plugin


def init_api(app):
    event_plagin = EventPlugin()
    permission_plagin = PermissionPlugin(strict=False)
    api_spec_plugin = create_api_spec_plugin(app)
    api = Api(app, plugins=[api_spec_plugin, event_plagin, permission_plagin, ])
    api.route(TagList, "tag_list", "/api/tags/", tag="Tag")
    api.route(TagDetail, "tag_detail", "/api/tags/<int:id>/", tag="Tag")
    api.route(ArticleList, "article_list", "/api/articles/", tag="Article")
    api.route(ArticleDetail, "article_detail", "/api/articles/<int:id>/", tag="Article")
    api.route(UsersList, "user_list", "/api/users/", tag="User")
    api.route(UserDetail, "user_detail", "/api/users/<int:id>/", tag="User")
    return api
