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
    
    users_list = User.query.all()

    return render_template("user_listing.html", users=users_list) 

# GET /users/new   
@app.route("/users/new")
def show_add_form():

    return render_template("new_user_form.html")

# POST /users/new
@app.route("/users/new", methods=["POST"])
def process_add_form():

    
    first_name = request.form.get("first-name")
    last_name = request.form.get("last-name")
    image_url = request.form.get("image-url")

    new_user = User(first_name, last_name, image_url)

    db.session.add(new_user)
    db.session.commit()
    
    return redirect("/users")


# GET /users/[user-id]
@app.route("/users/<int:id>")
def user_page(id):

    user_id = User.query.get_or_404(id)

    return render_template("user_detail.html", user=user_id)


