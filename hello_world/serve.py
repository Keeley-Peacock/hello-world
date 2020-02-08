from flask import Flask
from flask import render_template, send_from_directory
from hello_world import __version__
import os
from loguru import logger

app = Flask(__name__)


@app.route("/")
def hello():
    text = "You smell like fish"
    return render_template("index.html", message=text, version=__version__)


@app.route("/favicon.ico")
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, "static"),
        "favicon.ico",
        mimetype="image/vnd.microsoft.icon",
    )


if __name__ == "__main__":
    logger.info(os.path.join(app.root_path, "static"))
    app.run(debug=True)
