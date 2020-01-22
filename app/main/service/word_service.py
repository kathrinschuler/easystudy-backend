from app.main.models.word_model import WordModel


class ListService:
    def __init__(self):
        self.model = WordModel()

    def add_word(self, params):
        return self.model.create(params["original"], params["translation"], params["sentence"])

    def list(self):
        return self.model.list_words()

