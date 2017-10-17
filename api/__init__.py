from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

# init a Flask app
app = Flask(__name__)

# make it an flast_resful API
restfulAPI = Api(app)

# init SQLAlchemy
db = SQLAlchemy()

# configure a few things
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./myawesome.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from api.models.post import Post
from api.resources.hello import Hello

# connect to the db
db.init_app(app)

# expose API resources
restfulAPI.add_resource(Hello, '/hello')