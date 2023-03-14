from werkzeug.security import generate_password_hash
from blog.models import Article, Tag
from blog.app import crate_app, db

app = crate_app()


@app.cli.command('init-db')
def init_db():
    db.create_all()


@app.cli.command('create-user')
def create_user():
    from blog.models import User
    db.session.add(
        User(first_name='Феодора', email='fedora@gmail.ru', password=generate_password_hash('0000'))
    )
    db.session.add(
        User(first_name='Богдан', email='bogdan@gmail.ru', password=generate_password_hash('1111'))
    )
    db.session.add(
        User(first_name='Адам', email='adam@gmail.ru', password=generate_password_hash('2222'))
    )
    db.session.commit()


@app.cli.command('create-articles')
def create_articles():
    article_1 = Article(title="Руководство по SQLAlchemy в Flask",
                        text="В этом материале речь пойдет об основах SQLAlchemy. Создадим веб-приложение на Flask, фреймворке языка Python. Это будет минималистичное приложение, которое ведет учет книг."
                             "С его помощью можно будет добавлять новые книги, читать уже существующие, обновлять и удалять их. Эти операции — создание, чтение, обновление и удаление — также известны как «CRUD» и составляют основу почти всех веб-приложений. О них отдельно пойдет речь в статье."
                             "Прежде чем переходить к CRUD, разберемся с отдельными элементами приложения, начиная с SQLAlchemy.Стоит отметить, что существует расширение для Flask под названием flask-sqlalchemy, которое упрощает процесс использования SQLAlchemy с помощью некоторых значений по умолчанию и других элементов. Они в первую очередь облегчают выполнение базовых задач. Но в этом материале будет использоваться только чистый SQLAlchemy, чтобы разобраться в его основах без разных расширений.",
                        author=1
                        )
    article_2 = Article(title="Введение во Flask",
                        text="Flask — это микрофреймворк для Python, созданный в 2010 году разработчиком по имени Армин Ронахер. Но что значит это «микро»?"
                             "Это говорит о том, что Flask действительно маленький. У него в комплекте нет ни набора инструментов, ни библиотек, которыми славятся другим популярные фреймворки Python: Django или Pyramid. Но он создан с потенциалом для расширения. Во фреймворке есть набор базовых возможностей, а расширения отвечают за все остальное. «Чистый» Flask не умеет подключаться к базе данных, проверять данные формы, загружать файлы и так далее. Для добавления этих функций нужно использовать расширения. Это помогает использовать только те, которые на самом деле нужны."
                             "Flask также не такой жесткий в отношении того, как разработчик должен структурировать свою программу, в отличие от, например, Django где есть строгие правила. Во Flask можно следовать собственной схеме.",
                        author=2
                        )
    article_3 = Article(title="Аутентификация во Flask",
                        text="Аутентификация — один из самых важных элементов веб-приложений. Этот процесс предотвращает попадание неавторизованных пользователей на непредназначенные для них страницы. Собственную систему аутентификации можно создать с помощью куки и хэширования паролей. Такой миниатюрный проект станет отличной проверкой полученных навыков."
                             "Как можно было догадаться, уже существует расширение, которое может значительно облегчить жизнь. Flask-Login — это расширение, позволяющее легко интегрировать систему аутентификации в приложение Flask. Установить его можно с помощью следующей команды:"
                             "(env) gvido@vm:~/flask_app$  pip install flask-login",
                        author=3
                        )
    db.session.add_all([article_1, article_2, article_3])
    db.session.commit()


@app.cli.command("create-tags")
def create_tags():
    from blog.models import Tag
    for name in ["flask", "django", "python", "sqlalchemy", "news"]:
        tag = Tag(name=name)
        db.session.add(tag)
    db.session.commit()
    print("created tags")


if __name__ == '__main__':
    app.run(host='0.0.0.0')
