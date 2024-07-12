# inventory.py
# This module provides functions to interact with the Inventory table in the database.
# Functions include updating inventory records and retrieving inventory details by product ID.

from db.db_connection import get_db_connection

def update_inventory(product_id, quantity, cost_price, selling_price):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO Inventory (ProductID, Quantity, CostPrice, SellingPrice)
                      VALUES (?, ?, ?, ?)''', (product_id, quantity, cost_price, selling_price))
    conn.commit()
    conn.close()

def get_inventory(product_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Inventory WHERE ProductID = ?', (product_id,))
    inventory = cursor.fetchone()
    conn.close()
    return inventory
