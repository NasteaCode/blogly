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
    
    # don't need if instance syntax is used from alchemy
    # def __init__(self, first_name, last_name, image_url):
    #     self.first_name = first_name
    #     self.last_name = last_name
    #     self.image_url = image_url