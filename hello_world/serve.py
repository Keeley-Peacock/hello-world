from flask import Flask
from flask import render_template
from hello_world import __version__

app = Flask(__name__)


@app.route("/")
def hello():
    text = "You smell like fish"
    return render_template("index.html", message=text, version=__version__)


if __name__ == "__main__":
    app.run(debug=True)
