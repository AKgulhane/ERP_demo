# salespersons.py
# This module provides functions to interact with the SalesPersons table in the database.
# Functions include creating a new salesperson and retrieving salesperson details by salesperson ID.

from db.db_connection import get_db_connection

def create_salesperson(name, email):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO SalesPersons (Name, Email) VALUES (?, ?)', (name, email))
    conn.commit()
    conn.close()

def get_salesperson(salesperson_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM SalesPersons WHERE SalesPersonID = ?', (salesperson_id,))
    salesperson = cursor.fetchone()
    conn.close()
    return salesperson
