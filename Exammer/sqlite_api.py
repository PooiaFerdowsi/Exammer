import sqlite3
import os.path

from string import ascii_lowercase, ascii_uppercase

DB_PATH = 'sqlite.db'

if not os.path.isfile(DB_PATH):
    db = sqlite3.connect(DB_PATH)
    cursor = db.cursor()
    cursor.execute(open('sqls/create_table.sql').read())
    db.commit(); db.close(); del db; del cursor

TABLE_NAME = 'questions' # name of table just created

def check_table_name(table_name):
    r"""Is passed table name valid
    Valid table names must start with alphabet char..s or underscore(_).
    And only can contain alphanumeric characters and underscores(_).

    True if table name is valid.
    """
    if table_name[0] == "_" or table_name[0].isalpha():
        valids = ascii_lowercase + ascii_uppercase + '_'
        return set(table_name).issubset(set(valids))
    return False

def get_all(cursor: sqlite3.Cursor, table):
    if type(cursor) == sqlite3.Cursor and check_table_name(table):
        return cursor.execute(f"SELECT * FROM {table}").fetchall()
    return False

def get_eq(cursor: sqlite3.Cursor, table, **where):
    if type(cursor) != sqlite3.Cursor: return False
    if check_table_name(table) == False: return False
    text = ''
    for key, value in where.items():
        # add extra security cases
        text += f"{key}={value}"
    return cursor.execute(f"SELECT * FROM {table} WHERE {text}").fetchall()

def insert_spec(cursor: sqlite3.Cursor, table, **values): # complete
    keys = texts = ''
    for key, value in values.items():
        keys += key + ','

def insert_all(cursor: sqlite3.Cursor, table, values):
    cursor.execute(f"INSERT INTO {table} VALUES {values}")

def delete_eq(cursor: sqlite3.Cursor, table, **where):
    text = ''
    for key, value in where.items():
        text += f"{key}={value}"
    cursor.execute(f"DELETE FROM {table} WHERE {text}")