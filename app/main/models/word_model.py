import sqlite3
import uuid


class WordModel:
    WORDS_TABLE = "words"
    WORD_TO_LIST_TABLE = "word_to_list"
    LISTS_TABLE = "lists"

    def __init__(self):
        self.conn = sqlite3.connect('easystudy.db')

    def _find_or_create_word(self, original, translation):
        # Check if we have the word already
        query = f"SELECT id FROM {self.WORDS_TABLE} " \
                f"WHERE original = ? AND translation = ?"

        rows = self.conn.execute(query, [original, translation]).fetchone()
        if rows:
            return rows[0]

        # Insert
        word_id = str(uuid.uuid4())
        query = f"INSERT INTO {self.WORDS_TABLE} " \
                f"(id, original, translation) " \
                f"VALUES (?, ?, ?)"
        self.conn.execute(query, [word_id, original, translation])
        self.conn.commit()
        print(f"Word id: {word_id}")
        return word_id

    def add_word_to_list(self, list_id, original, translation):
        word_id = self._find_or_create_word(original, translation)
        query = f"INSERT INTO {self.WORD_TO_LIST_TABLE} " \
                f"(word_id, list_id) " \
                f"VALUES (?, ?)"
        result = self.conn.execute(query, [word_id, list_id])
        self.conn.commit()
        #TODO: Check if the word was already in the list/insert will fail in this case

    def get_words_in_list(self, list_id):
        columns = ['id', 'original', 'translation']
        query = f"SELECT {','.join(columns)} " \
                f"from {self.WORDS_TABLE} w JOIN {self.WORD_TO_LIST_TABLE} wtl " \
                f"ON w.id = wtl.word_id WHERE wtl.list_id = ?"
        result_set = self.conn.execute(query, [list_id]).fetchall()

        result = [{col: word[i] for i, col in enumerate(columns)}
                  for word in result_set]
        return result
