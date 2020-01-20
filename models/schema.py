import sqlite3


def setup_tables():
    conn = sqlite3.connect('easystudy.db')
    create_lists_table(conn)
    create_words_table(conn)
    create_mapping_table(conn)


def create_lists_table(conn):
    query = """
    CREATE TABLE IF NOT EXISTS "lists" (
      id TEXT PRIMARY KEY,
      title TEXT,
    );
    """
    conn.execute(query)


def create_words_table(conn):
    query = """
    CREATE TABLE IF NOT EXISTS "words" (
      id TEXT PRIMARY KEY,
      original TEXT NOT NULL,
      translation TEXT NOT NULL,
      sentence_original TEXT,
      sentence_translation TEXT,
    );
    """

    conn.execute(query)


def create_mapping_table(conn):
    query = """
    CREATE TABLE IF NOT EXISTS "word_to_list" (
        word_id TEXT,
        list_id TEXT,
        CONSTRAINT word_list PRIMARY KEY (word_id, list_id),
        FOREIGN KEY(word_id) REFERENCES words(id),
        FOREIGN KEY(list_id) REFERENCES lists(id)
    );
    """
    conn.execute(query)
