from flask import url_for
from flask_admin import expose, AdminIndexView
from flask_login import current_user
from flask_admin.contrib.sqla import ModelView
from werkzeug.utils import redirect


class CustomView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('auth.login'))


class MyAdminIndexView(AdminIndexView):
    @expose("/")
    def index(self):
        if not (current_user.is_authenticated):
            return redirect(url_for("auth.login"))
        return super(MyAdminIndexView, self).index()


class TgAdminView(CustomView):
    column_searchable_list = ("name",)
    column_filters = ("name",)
    can_export = True
    export_types = ['csv', 'xlsx']
    create_modal = True
    edit_modal = True


class UserAdminView(CustomView):
    column_exclude_list = ("password")
    column_searchable_list = ("first_name", "last_name", "email", "age")
    column_filters = ("first_name", "last_name", "email", "age")
    column_editable_list = ("first_name", "last_name", "email", "age")
    can_create = True
    can_edit = True
    can_delete = True


class ArticleAdminView(CustomView):
    can_export = True
    export_types = ('csv', 'xlsx')
    column_filters = ('author',)
    can_create = True
    can_edit = True
    can_delete = True
