from flask import Flask, Response, request
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def index():
    name = request.args.get('name', None)
    data_now = datetime.now()
    return Response(f"Привет, {name if name is not None else 'друг'}/"
                    f"{data_now.strftime('%d %B %Y')}")


@app.errorhandler(404)
def handler_404(msg):
    app.logger.error(msg)
    return Response('Ошибочка....')
