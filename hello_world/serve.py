from flask import Flask
from flask import render_template

# creates a Flask application, named app
app = Flask(__name__)


@app.route("/")
def hello():
    text = "You smell like fish"
    return render_template('index.html', message=text)


if __name__ == "__main__":
    app.run(debug=True)
