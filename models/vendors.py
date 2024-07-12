# vendors.py
# This module provides functions to interact with the Vendors table in the database.
# Functions include creating a new vendor, retrieving vendor details by vendor ID, and retrieving all vendors.

from db.db_connection import get_db_connection

def create_vendor(name, address, email):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Vendors (Name, Address, Email) VALUES (?, ?, ?)', (name, address, email))
    conn.commit()
    conn.close()

def get_vendor(vendor_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Vendors WHERE VendorID = ?', (vendor_id,))
    vendor = cursor.fetchone()
    conn.close()
    return vendor

def get_all_vendors():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Vendors')
    vendors = cursor.fetchall()
    conn.close()
    return vendors

