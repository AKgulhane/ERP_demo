# db_connection.py
# This module establishes a connection to the SQLite database for the ERP system.
# It provides a function, get_db_connection, which returns a database connection object.
# This module is used by other parts of the application to interact with the database.

import sqlite3

def get_db_connection():
    conn = sqlite3.connect('erp_system.db')
    return conn
