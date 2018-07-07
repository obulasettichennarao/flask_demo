
from flask import Flask
from flask_restplus import Resource, Api
from flask_marshmallow import Marshmallow

app = Flask(__name__)

ma = Marshmallow(app)


from api import api_blueprint
app.register_blueprint(api_blueprint)


__all__ = ['app']
if __name__ == '__main__':
    app.run(debug=True)
