from flask import Flask, request, jsonify
from app.main.models.db_accessor import setup_tables
from app.main.service.list_service import ListService
from app.main.service.word_service import WordService

app = Flask(__name__)


# List related methods
@app.route("/lists", methods=["GET"])
def get_all_lists():
    return jsonify(ListService().get_all_lists())


@app.route("/lists", methods=["POST"])
def create_new_list():
    return ListService().create_list(request.get_json())


@app.route("/lists/<list_id>", methods=["GET"])
def get_list(list_id):
    pass


@app.route("/lists/<list_id>", methods=["PUT"])
def update_list(list_id):
    pass


@app.route("/lists/<list_id>", methods=["DELETE"])
def delete_list(list_id):
    pass


# Word related methods
@app.route("/lists/<list_id>/words", methods=["GET"])
def get_words_in_list(list_id):
    return jsonify(WordService().get_words_in_list(list_id))


@app.route("/lists/<list_id>/words", methods=["POST"])
def add_word_to_list(list_id):
    return WordService().add_word_to_list(list_id, request.get_json())


@app.route("/lists/<list_id>/words/<word_id>", methods=["DELETE"])
def delete_word_from_list(list_id):
    pass


@app.route("/lists/<list_id>/words/<word_id>", methods=["GET"])
def get_word(list_id, word_id):
    # TBD what this can do, could link to some overview page of how this word is used?
    pass


if __name__ == "__main__":
    setup_tables()
    app.run(debug=True)
