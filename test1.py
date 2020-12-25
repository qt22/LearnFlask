from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "anykey"
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///users.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.permanent_session_lifetime = timedelta(minutes=60)

db = SQLAlchemy(app)

class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))

    def __init__(self, name, email):
        self.name = name
        self.email = email




@app.route("/")
def home():
    return render_template("index.html")

@app.route("/view/", methods=["POST", "GET"])
def view():
    if request.method == "POST":
        email = request.form["email"]
        users.query.filter_by(email=email).delete()
        db.session.commit()
    return render_template("view.html", values=users.query.all())

@app.route("/login/", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        username = request.form["nm"]  # get data
        session["username"] = username

        found_user = users.query.filter_by(name=username).first()
        if found_user:
            session["email_address"] = found_user.email
        else:
            usr = users(username, "")
            db.session.add(usr) 
            db.session.commit()

        flash("log in successful!")
        return redirect(url_for("user"))
    else:
        if "username" in session:
            flash("already logged in!")
            return redirect(url_for("user"))
    return render_template("login.html")

@app.route("/user/", methods=["POST", "GET"])
def user():
    email = None
    if "username" in session:
        username = session["username"]
        if request.method == "POST":
            email = request.form["email"]  # html name property
            session["email_address"] = email

            found_user = users.query.filter_by(name=username).first()
            found_user.email = email
            db.session.commit()

            flash("Email was saved!")
        else:
            if "email_address" in session:
                email = session["email_address"]
        return render_template("user.html", email_address=email, user=username)
    else:
        flash("you are not logged in!")
        return redirect(url_for("login"))
    
@app.route("/logout/", methods=["POST", "GET"])
def logout():
    if request.method == "POST" and "username" in session:
        username = session["username"]
        session.pop("username", None)
        flash(f"You have been logged out, {username}!!!", "info")
        return redirect(url_for("login"))
    elif request.method == "GET":
        return render_template("logout.html")
    

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)







### Lesson 1: Introduction to Flask
# @app.route("/<cityName>")
# def city(cityName):
#     return f"Are you from {cityName}"

# @app.route("/admin/")
# def admin():
#     return redirect(url_for("city", cityName="wuhan"))
### Lesson 1






### Lesson 3: Templates
# @app.route("/test")
# def test():
#     return render_template("test.html")
### Lesson 3






### Lesson 4: GET & POST
# @app.route("/login/", methods=["POST", "GET"])
# def login():
#     if request.method == "POST":
#         username = request.form["nm"] # get data 
#         return redirect(url_for("user", usr=username))
#     else:
#         return render_template("login.html")
    

# @app.route("/<usr>")
# def user(usr):
#     return f"<h1>{usr}<h1>"
### Lesson 4






### Lesson 5
# @app.route("/login/", methods=["POST", "GET"])
# def login():
#     if request.method == "POST":
#         session.permanent = True
#         username = request.form["nm"]  # get data
#         session["username"] = username
#         return redirect(url_for("user"))
#     else:
#         return render_template("login.html")

# @app.route("/user")
# def user():
#     if "username" in session:
#         username = session["username"]
#         return f"<h1>{username}<h1>"
#     else:
#         return redirect(url_for("login"))
    
# @app.route("/logout", methods=["POST", "GET"])
# def logout():
#     if request.method == "POST":
#         session.pop("username", None)
#         return redirect(url_for("login"))
#     else:
#         return render_template("logout.html")
# ### Lesson 5