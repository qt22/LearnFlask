from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>hello there general kenobi</h1>"

@app.route("/<streetName>")
def street(streetName):
    return f"you belong to {streetName}"

@app.route("/admin")
def admin():
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run()
