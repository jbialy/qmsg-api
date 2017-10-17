from api import db

class Post(db.Model):

    ## this class defines the Post table
    #
    __tablename__ = 'post'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, unique=False, nullable=False) ## this would normally be a relationship to an id in anothert table
    post = db.Column(db.String(255), unique=False)
    date_created  = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __init__(self, user_id, post):
        ## init the post and link it to a user
        self.user_id = user_id
        self.post = post
    
    def save(self):
        ## commit the actual post to the database
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        ## a string representation of the Post object
        return "<Post: {}>".format(self.id)
