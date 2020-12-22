from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login/", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form["nm"] # get data 
        return redirect(url_for("user", usr=username))
    else:
        return render_template("login.html")
    

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}<h1>"




if __name__ == "__main__":
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
