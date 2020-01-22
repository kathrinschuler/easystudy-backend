import sqlite3
from pathlib import Path

def setup_tables():
    conn = sqlite3.connect('easystudy.db')
    with open(Path('main/models/db_schema.sql')) as query_file:
        conn.executescript(query_file.read())
