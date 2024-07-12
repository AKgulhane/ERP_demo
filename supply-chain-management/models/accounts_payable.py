# accounts_payable.py
# This module provides functions to interact with the AccountsPayable table in the database.
# Functions include creating a new accounts payable record and retrieving accounts payable details by invoice ID.

from db.db_connection import get_db_connection

def create_accounts_payable(vendor_id, invoice_date, due_date, amount_due, status='Open'):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO AccountsPayable (VendorID, InvoiceDate, DueDate, AmountDue, Status)
                      VALUES (?, ?, ?, ?, ?)''', (vendor_id, invoice_date, due_date, amount_due, status))
    conn.commit()
    conn.close()

def get_accounts_payable(invoice_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM AccountsPayable WHERE InvoiceID = ?', (invoice_id,))
    invoice = cursor.fetchone()
    conn.close()
    return invoice
