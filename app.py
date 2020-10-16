from flask import Flask, request, redirect, render_template
from models import db, connect_db, User, Post
# import DateNow

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

    return render_template("users.html", users=users_list) 

# GET /users/new   
@app.route("/users/new")
def show_add_form():

    return render_template("users/new.html")

# POST /users/new
@app.route("/users/new", methods=["POST"])
def process_add_form():

    
    first_name = request.form.get("first-name")
    last_name = request.form.get("last-name")
    image_url = request.form.get("image-url")

    new_user = User(first_name=first_name, last_name=last_name, image_url=image_url)

    db.session.add(new_user)
    db.session.commit()
    
    return redirect("/users")


# GET /users/[user-id]
@app.route("/users/<int:id>")
def user_page(id):

    user = User.query.get_or_404(id)
    # breakpoint()
    return render_template("users/[user-id].html", user=user)

# GET /users/[user-id]/edit
@app.route("/users/<int:id>/edit")
def show_edit_user(id):

    user = User.query.get_or_404(id)

    return render_template("users/[user-id]/edit.html", user=user)


# POST /users/[user-id]/edit
@app.route("/users/<int:id>/edit", methods=["POST"])
def update_user(id):

    user = User.query.get(id)
    user.first_name = request.form.get("first_name")
    user.last_name = request.form.get("last_name")
    user.image_url = request.form.get("image_url")
    
    db.session.commit()

    return redirect("/users")

# POST /users/[user-id]/delete
@app.route("/users/<int:id>/delete")
def delete_user(id):

    user = User.query.get(id)

    db.session.delete(user)

    db.session.commit()

    return redirect("/users")

# GET /users/[user-id]/posts/new
@app.route("/users/<int:id>/posts/new")
def show_add_post_form(id):

    user = User.query.get_or_404(id)

    return render_template("/users/[user-id]/posts/new.html", user=user)

# POST /users/[user-id]/posts/new
@app.route("/users/<int:id>/posts/new", methods=["POST"])
def add_post(id):

    title = request.form.get("title")
    content = request.form.get("content")
    user = User.query.get_or_404(id)

    new_post = Post(title=title, content=content, user=user)

    db.session.add(new_post)
    db.session.commit()
    
    return redirect(f"/users/{id}")

# GET /posts/[post-id]
@app.route("/posts/<int:post_id>")
def show_post(post_id):

    post = Post.query.get_or_404(post_id)
    return render_template("/posts/[post-id].html", post=post)

# GET /posts/[post-id]/edit
@app.route("/posts/<int:post_id>/edit")
def show_post_edit_form(post_id):

    post = Post.query.get_or_404(post_id)
    return render_template("/posts/[post-id]/edit.html", post=post)

# POST /posts/[post-id]/edit
# @app.route("/posts/<int:post_id>/edit")
# def edit_post(post_id):



# POST /posts/[post-id]/delete
@app.route("/posts/<int:post_id>/delete", methods=["POST"])
def delete_post(post_id):

    post = POST.query.get_or_404(post_id)

    db.session.delete(post)

    db.session.commit()

    return redirect(f"/users/{post.user_id}")

