# api/__init__.py

from flask import Flask
from flask_restful import Api
# import the the db object and models
from api.models import db

# init a Flask app
application = Flask(__name__)
# map the application back to app
app = application

# make it an flast_resful API
restfulAPI = Api(app)

# configure a few things
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./myawesome.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from api.resources import PostListResource, PostResource, RootResource

# connect to the db
db.init_app(app)

# switch to app context and provision tables
# reference : http://flask-sqlalchemy.pocoo.org/2.3/contexts/
with app.app_context():
    db.create_all()

# expose API resources
restfulAPI.add_resource(RootResource, '/')
restfulAPI.add_resource(PostResource, '/post', '/post/<int:post_id>')
restfulAPI.add_resource(PostListResource, '/posts')