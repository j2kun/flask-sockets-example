import os

import rethinkdb as r
from rethinkdb.errors import RqlRuntimeError


RDB_HOST = os.environ.get('RDB_HOST', 'localhost')
RDB_PORT = os.environ.get('RDB_PORT', '28015')
DB_NAME = 'example'


# Setting up the app database
def init():
    connection = r.connect(host=RDB_HOST, port=RDB_PORT)
    try:
        r.db_create(DB_NAME).run(connection)
        r.db(DB_NAME).table_create('chat').run(connection)
        print('Database setup completed.')
    except RqlRuntimeError:
        print('App database already exists.')
    finally:
        connection.close()


if __name__ == "__main__":
    init()
