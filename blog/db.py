import sqlite3
from sqlite3 import Error
from flask import current_app, g
import os 

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'DbBlogs.db')

def get_db():
    try:
        if 'db' not in g:
            g.db = sqlite3.connect(my_file)
        return g.db
    except Error:
        print(Error)


def close_db():
    db = g.pop( 'db', None )

    if db is not None:
        db.close()