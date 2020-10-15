from flask import Flask, request, redirect, render_template
from models import db, connect_db, User

"""Blogly application."""



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

# GET /
@app.route("/")
def redirect_list_users():
    
    return redirect("/users")


@app.route("/users")
def user_listing():
    
    return render_template("user_listing.html") 

# GET /users/new   
@app.route("/users/new")
def show_add_form():

    return render_template("new_user_form.html")

# POST /users/new
@app.route("/users/new", methods=["POST"])
def process_add_form():

    
    first_name = request.form("first-name")
    last_name = request.form("last-name")
    image_url = request.form("image-url")

    new_user = User(first_name, last_name, image_url)
    db.session.add(new_user)
    db.session.commit()
    
    return redirect("/users")

