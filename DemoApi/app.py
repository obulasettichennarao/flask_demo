import json
from flask import Response
from config import app
from werkzeug.contrib.fixers import ProxyFix
from settings import Settings
app.secret_key = Settings.SECRET_KEY
app.wsgi_app = ProxyFix(app.wsgi_app)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=Settings.LISTEN_PORT)
