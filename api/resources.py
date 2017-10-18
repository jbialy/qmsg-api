# api/resources.py

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
            obj = {'post_id': post.id, 'user_id': post.user_id, 'message': post.message}
            results.append(obj)
        return results
#
# define /post endpoint
#  
class PostResource(Resource):

    def get(self, post_id=None):
        # check to see received a post_id
        if (post_id == None):
            return {'message' : 'get request must contain a post_id'}

        #
        # the function accepts a string and checks to see if it's a palindrome
        # returns: True or False
        # 
        def is_palindrome(message):
            ## let's check if the post is a palindrome 
            message_stripped = message.replace(" ", "")
            # traverses the string, comparing char at pos[0+N] to pos[STRLENGTH-N]
            # if all chars are equal then we have a palindrome!
            palindrome = True
            for pos, char in enumerate(message_stripped):
                msg_len = len(message_stripped)-1
                if (char != message_stripped[msg_len-pos]):
                    # as soon as we don't find a match break out
                    palindrome = False
                    break
            return palindrome

        # move some of the logic to the PostModel object?
        result = PostModel.query.filter_by(id=post_id).first()
        # form an error response
        response = {'message' : 'no posts found for this post_id'}
        if (result):
            # return the actual query results
            response = { 'user_id' : result.user_id, 'post' : result.message, "palindrome" : is_palindrome(result.message)}
        return response

    def post(self):
        args = parser.parse_args()
        # create a new post using the arguments received and save it!
        new_post = PostModel(args['user_id'], args['message'])
        new_post.save()
        # simply return the new post
        return {'user_id' : args['user_id'], 'message' : args['message']}, 201

#
# define / endpoint
#  
class RootResource(Resource):
    def get(self):
        # return a simple clean response
        return {'message' : 'welcome to qmsg-api'}
