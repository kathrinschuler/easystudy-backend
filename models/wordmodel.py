import sqlite3


class WordModel:
    TABLENAME = "words"

    def __init__(self):
        self.conn = sqlite3.connect('easystudy.db')

    def create(self, original, translation, sentence):
        query = f"INSERT INTO {self.TABLENAME} " \
                f"(original, translation, sentence) " \
                f"VALUES ('{original}','{translation}', '{sentence}')"
        result = self.conn.execute(query)
        self.conn.commit()
        return str(result.lastrowid)

    def list_words(self):
        columns = ['original', 'translation', 'sentence']
        query = f"SELECT {','.join(columns)} " \
                f"from {self.TABLENAME} WHERE TRUE"
        result_set = self.conn.execute(query).fetchall()

        result = [{col: word[i] for i, col in enumerate(columns)}
                  for word in result_set]
        return result
