from combojsonapi.permission.permission_system import PermissionMixin, PermissionUser, PermissionForGet
from flask_combo_jsonapi.exceptions import AccessDenied
from flask_login import current_user
from blog.models.models import User


class UserPermission(PermissionMixin):
    ALL_AVAILABLE_FIELDS = [
        "id",
        "first_name",
        "last_name",
        "email",
        "age"
    ]

    def get(self, *args, many=True, user_permission: PermissionUser = None, **kwargs) -> PermissionForGet:
        if not current_user.is_authenticated:
            raise AccessDenied("no access")
        self.permission_for_get.allow_columns = (self.ALL_AVAILABLE_FIELDS, 10)
        return self.permission_for_get
