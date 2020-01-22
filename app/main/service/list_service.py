from app.main.models.list_model import ListModel


class ListService:
    def __init__(self):
        self.model = ListModel()

    def create_list(self, params):
        # TODO: error handling if insert fails
        list_id = self.model.create_list(params['title'])
        response_object = {
            'listId': list_id,
            'title': params['title']
        }

        return response_object, 201, {'Location': f'/lists/{list_id}'}

    def get_all_lists(self):
        return self.model.get_all_lists()

