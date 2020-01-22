from app.main.models.word_model import WordModel


class WordService:
    def __init__(self):
        self.model = WordModel()

    def add_word_to_list(self, list_id, params):
        # TODO: error handling if insert fails

        self.model.add_word_to_list(
            list_id,
            params['original'],
            params['translation']
        )
        response_object = {
            'listId': list_id,
            'original': params['original'],
            'translation': params['translation']
        }

        return response_object, 201, {'Location': f'/lists/{list_id}/words'}

    def get_words_in_list(self, list_id):
        return self.model.get_words_in_list(list_id)
