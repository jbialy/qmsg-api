from flask_restful import Resource, reqparse
from api.models import PostModel

# create a request parser and add argument that it should look for in the request
parser = reqparse.RequestParser()
# we need the request to contain a user_id and a message
parser.add_argument('user_id', type=int, required=True)
parser.add_argument('message', required=True)

#
# define /posts endpoint
#  
class PostListResource(Resource):
    def get(self):
        # fetch all the posts
        posts = PostModel.query.all()
        results = []
        # go through all the post objects and add them as individual lists to an array
        for post in posts:
            obj = {'id': post.id, 'user_id': post.user_id, 'message': post.message}
            results.append(obj)
        return results
#
# define /post endpoint
#  
class PostResource(Resource):
    def get(self, post_id):
        # change to to better utilize the PostModel object?
        result = PostModel.query.filter_by(id=post_id).first()
        return { 'user_id' : result.user_id, 'post' : result.message}

    def post(self):
        args = parser.parse_args()
        # create a new post using the arguments received and save it!
        new_post = PostModel(args['user_id'], args['message'])
        new_post.save()
        # simply return the new post
        return {int(args['user_id']) : args['message']}, 201