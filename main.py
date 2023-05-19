from flask import json
import sentry_sdk

from flask import Flask
from sentry_sdk.integrations.flask import FlaskIntegration
from werkzeug.exceptions import HTTPException
from flask import Flask, request, jsonify


sentry_sdk.init(
    dsn="https://5b5a8d2025554dd4af8688d49d2b8021@o4505165547962368.ingest.sentry.io/4505209375490048",
    integrations=[FlaskIntegration()],
)

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello, World!'


@app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    # начнем с правильных заголовков и кода состояния из ошибки
    response = e.get_response()
    # заменить тело на JSON
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response


@app.route('/error')
def error():
    return (1 / 0)

# неправильно использованная функция запроса


@app.route('/login')
def login():
    username = request.GET.get('username')
    password = request.GET.get('password')

    # обработка ошибок
    if not username or not password:
        return jsonify({'error': 'Invalid username or password'}), 400

    # аутентификация пользователя
    # ...

    return jsonify({'success': True})

# неправильно настроенный маршрут


@app.route('/user/<int:user_id>')
def get_user(user_id):
    user = db.get_user(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    return jsonify(user)


if __name__ == '__main__':
    app.run()
