# api/models.py

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class PostModel(db.Model):

    ## this class defines the Post table
    #
    __tablename__ = 'post'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, unique=False, nullable=False) ## this would normally be a relationship to an id in anothert table
    message = db.Column(db.String(255), unique=False, nullable=False)
    date_created  = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __init__(self, user_id, message):
        ## init the post and link it to a user
        self.user_id = user_id
        self.message = message
    
    def save(self):
        ## commit the actual post to the database
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        ## a friendly representation of the PostModel object
        return "<PostModel: {}>".format(self.id)
