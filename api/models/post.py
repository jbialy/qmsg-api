from api import db

class Post(db.Model):

    __tablename__ = 'post'

    id = db.Column(db.Integer, primary_key=True)
    post = db.Column(db.String(80), unique=False, nullable=False)
    date_created  = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return '<Post %r>' % self.id
