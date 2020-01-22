import sqlite3
import uuid

class ListModel:
    TABLENAME = "lists"

    def __init__(self):
        self.conn = sqlite3.connect('easystudy.db')

    def create_list(self, title):
        list_id = str(uuid.uuid4())
        query = f"INSERT INTO {self.TABLENAME} " \
                f"(id, title) " \
                f"VALUES (?,?)"
        self.conn.execute(query, [list_id, title])
        self.conn.commit()

    def get_all_lists(self):
        column_names = ['id', 'title']
        query = f"SELECT {','.join(column_names)} " \
                f"FROM {self.TABLENAME} WHERE TRUE"
        result_set = self.conn.execute(query).fetchall()
        result = [{col: word_list[i] for i, col in enumerate(column_names)}
                  for word_list in result_set]
        return result
