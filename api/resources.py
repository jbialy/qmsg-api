from flask_restful import Resource
from api.models import Post

class Hello(Resource):
    def get(self):
        return {'hello': 'world'}