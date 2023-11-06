import os

from flask import Flask, jsonify, render_template, send_from_directory

from .utils import get_word

app = Flask(__name__)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(directory=os.path.join(app.root_path, "static"), path="favicon.png")


@app.route("/")
def index():
    return render_template("game.html")


@app.route("/get-spy-word", methods=["GET"])
def get_spy_word():
    spy_word = get_word()
    return jsonify({"spyWord": spy_word})


@app.route("/info")
def info():
    return jsonify({"version": "0.1.0"})


if __name__ == "__main__":
    app.run()
