from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route("/<userName>")
def home(userName):
    return render_template("index.html", content="welcome "+userName, anime=["mob psycho 100", "haikyuu", "attack on titan"])



### Lesson 1: Introduction to Flask
# @app.route("/<cityName>")
# def city(cityName):
#     return f"Are you from {cityName}"

# @app.route("/admin/")
# def admin():
#     return redirect(url_for("city", cityName="wuhan"))
### Lesson 1

if __name__ == "__main__":
    app.run()
