from flask import Blueprint, render_template, redirect
from werkzeug.exceptions import NotFound

USERS = {1: {'name': 'Феодора', 'birthday': '12.04.1978',
             'description': 'Независимый, оригинальный, нетерпеливый, требовательный, ребячливый, жизнерадостный, любит забавы, склонен к риску, бесцеремонный, вызывающий, фантазер, своевольный, возбуждающий, назойливый, тщеславный'},
         2: {'name': "Богдан", 'birthday': '24.06.2000',
             'description': 'Активный, дерзкий, романтичный, интуитивный, независимый, оригинальный, нетерпеливый, требовательный, ребячливый'},
         3: {'name': "Адам", 'birthday': '11.05.1996',
             'description': 'Импульсивный, страстный, динамичный, доминирующий, гордый, бестактный, оптимистичный'}}
user = Blueprint('user', __name__, url_prefix="/users", static_folder="../static")


@user.route('/')
def user_list():
    return render_template('users/list.html', users=USERS)


@user.route('/<int:pk>')
def get_user(pk: int):
    try:
        user = USERS[pk]
    except KeyError:
        # raise NotFound(f"User id {pk} not found")
        return redirect("/users/")
    return render_template('users/details.html', user=user)
