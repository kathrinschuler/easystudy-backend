import sqlite3


class Schema:
    def __init__(self):
        self.conn = sqlite3.connect('easystudy.db')
        self.create_lists_table()
        self.create_words_table()

    def create_lists_table(self):
        pass

    def create_words_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS "words" (
          original TEXT,
          translation TEXT,
          sentence TEXT,
          CONSTRAINT original_translation PRIMARY KEY (original, translation)
        );
        """

        self.conn.execute(query)

