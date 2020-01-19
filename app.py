from flask import Flask, request, jsonify
from models.schema import Schema
from service.service import EasyStudyService

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/<name>")
def hello_name(name):
    return "Hello " + name


@app.route("/word", methods=["POST"])
def add_word():
    return EasyStudyService().add_word(request.get_json())


@app.route("/word", methods=["GET"])
def list_words():
    return jsonify(EasyStudyService().list())


if __name__ == "__main__":
    Schema()
    app.run(debug=True)
