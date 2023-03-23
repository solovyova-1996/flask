from marshmallow_jsonapi import Schema, fields
from combojsonapi.utils import Relationship


class TagShema(Schema):
    class Meta:
        type_ = 'tag'
        self_url = 'tag_detail'
        self_url_kwargs = {'id': '<id>'}
        self_url_many = 'tag_list'

    id = fields.Integer(as_string=True)
    name = fields.String(allow_none=False, required=True)


class UserShema(Schema):
    class Meta:
        type_ = 'user'
        self_url = 'user_detail'
        self_url_kwargs = {'id': '<id>'}
        self_url_many = 'user_list'

    id = fields.Integer(as_string=True)
    first_name = fields.String(allow_none=False, required=True)
    last_name = fields.String(allow_none=False)
    email = fields.String(allow_none=False, required=True)
    age = fields.Integer(as_string=True)


class ArticleShema(Schema):
    class Meta:
        type_ = 'article'
        self_url = 'article_detail'
        self_url_kwargs = {'id': '<id>'}
        self_url_many = 'article_list'

    id = fields.Integer(as_string=True)
    title = fields.String(allow_none=False, required=True)
    text = fields.String(allow_none=False, required=True)
    date = fields.DateTime(allow_none=False)
    author = Relationship(
        nested="UserShema",
        attribute="user",
        related_view="user_list",
        related_view_kwargs={"id": "<id>"},
        schema="UserShema",
        type_="user",
        many=False,
    )
    tags = Relationship(
        nested="TagShema",
        attribute="tags",
        related_view="user_list",
        related_view_kwargs={"id": "<id>"},
        schema="TagShema",
        type_="tag",
        many=False,
    )
