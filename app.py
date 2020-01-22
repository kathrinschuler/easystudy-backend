from flask import Flask, request, jsonify
from models.db_accessor import Schema
from service.service import EasyStudyService

app = Flask(__name__)


@app.route("/lists", methods=["GET"])
def get_all_lists():
    pass


@app.route("/lists", methods=["POST"])
def create_new_list():
    pass


@app.route("/lists/<list_id>", methods=["GET"])
def get_list(list_id):
    pass


@app.route("/lists/<list_id>", methods=["DELETE"])
def delete_list(list_id):
    pass


@app.route("/lists/<list_id>", methods=["POST"])
def update_list(list_id):
    pass


@app.route("/lists/<list_id>/words", methods=["GET"])
def get_words_for_list(list_id):
    pass
    # return EasyStudyService().add_word(request.get_json())


@app.route("/lists/<list_id>/words", methods=["POST"])
def add_word_to_list(list_id):
    pass


@app.route("/lists/<list_id>/words/<word_id>", methods=["DELETE"])
def delete_word_from_list(list_id):
    pass


if __name__ == "__main__":
    Schema()
    app.run(debug=True)
