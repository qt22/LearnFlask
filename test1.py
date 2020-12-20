from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route("/<userName>")
def home(userName):
    return render_template("index.html")

@app.route("/test")
def test():
    return render_template("test.html")

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

