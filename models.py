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
    
    image_url = db.Column(db.String(50),
                          nullable=False,
                          unique=True)
    

   