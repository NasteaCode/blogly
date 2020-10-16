import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Connect this database to provided Flask app. You should call this in your Flask app.     """
    db.app = app
    db.init_app(app)
    

"""Models for Blogly."""
class User(db.Model):
    """USER."""

    __tablename__ = "users"

    id = db.Column(db.Integer,
                  primary_key=True,
                  autoincrement=True)

    first_name = db.Column(db.String(20),
                           nullable=False,
                           unique=False)

    last_name = db.Column(db.String(20),
                          nullable=False,
                          unique=False)
    
    image_url = db.Column(db.String(120),
                          nullable=True,
                          unique=False)
    
    post = db.relationship("Post")
    
    # don't need if instance syntax is used from alchemy
    # def __init__(self, first_name, last_name, image_url):
    #     self.first_name = first_name
    #     self.last_name = last_name
    #     self.image_url = image_url

class Post(db.Model):

    __tablename__ = "posts"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)

    title = db.Column(db.String(50),
                      nullable=False)

    content = db.Column(db.String(1000),
                        nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
                           
    
    user_id = db.Column(db.Integer,
                        db.ForeignKey('users.id'))

    user = db.relationship("User")