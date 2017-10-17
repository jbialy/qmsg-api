from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
# import resource modules
from api.resources.hello import Hello

# init a Flask app
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./myawesome.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# init flask_restful
api = Api(app)

# init SQLAlchemy
db = SQLAlchemy(app)

# import database models
from api.models.post import Post

# create the db tables (this will not overwrite an existing database) 
#
db.create_all()

# expose a basic resource
api.add_resource(Hello, '/hello')