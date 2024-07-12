# sales.py
# This module provides functions to interact with the Sales table in the database.
# Functions include creating a new sale and retrieving sale details by sale ID.

from db.db_connection import get_db_connection

def create_product(name, description, price):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Products (Name, Description, Price) VALUES (?, ?, ?)', (name, description, price))
    conn.commit()
    conn.close()

def get_product(product_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Products WHERE ProductID = ?', (product_id,))
    product = cursor.fetchone()
    conn.close()
    return product
