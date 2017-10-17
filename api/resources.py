from flask_restful import Resource
from api.models import PostModel

class PostListResource(Resource):
    def get(self):
        posts = PostModel.query.all()
        results = []
        # go through all the post objects and add them as individual lists to an array
        for post in posts:
            obj = {'id': post.id, 'user_id': post.user_id, 'message': post.message}
            results.append(obj)
        return results

class PostResource(Resource):
    def get(self):
        newPost = PostModel(12, "this is my post number one")
        newPost.save()
        return {'heloooo': 'wwwworld'}