# customers.py
# This module provides functions to interact with the Customers table in the database.
# Functions include creating a new customer and retrieving customer details by customer ID.

from db.db_connection import get_db_connection

def create_customer(name, address, email):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Customers (Name, Address, Email) VALUES (?, ?, ?)', (name, address, email))
    conn.commit()
    conn.close()

def get_customer(customer_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Customers WHERE CustomerID = ?', (customer_id,))
    customer = cursor.fetchone()
    conn.close()
    return customer
