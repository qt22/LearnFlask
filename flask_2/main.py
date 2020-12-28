from flask import Flask, render_template
from another.second import second

app = Flask(__name__)
app.register_blueprint(second, url_prefix="/loo")

@app.route("/")
def home():
    return "<h1>hello there general grievous<h1>"


if __name__ == "__main__":
    app.run(debug=True)