from flask_restful import Api
from flask import Flask
from users import User

app = Flask(__name__)
api = Api(app)

api.add_resource(User, '/users', '/users/<int:id>')

if __name__ == '__main__':
    app.run(port=8000, host="0.0.0.0")