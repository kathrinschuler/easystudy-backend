import sqlite3


def setup_tables():
    conn = sqlite3.connect('easystudy.db')
    conn.executescript('db_schema.sql')
