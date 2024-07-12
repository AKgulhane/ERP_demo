# accounts_receivable.py
# This module provides functions to interact with the AccountsReceivable table in the database.
# Functions include creating a new accounts receivable record and retrieving accounts receivable details by invoice ID.

from db.db_connection import get_db_connection

def create_accounts_receivable(customer_id, invoice_date, due_date, amount_due, status='Open'):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO AccountsReceivable (CustomerID, InvoiceDate, DueDate, AmountDue, Status)
                      VALUES (?, ?, ?, ?, ?)''', (customer_id, invoice_date, due_date, amount_due, status))
    conn.commit()
    conn.close()

def get_accounts_receivable(invoice_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM AccountsReceivable WHERE InvoiceID = ?', (invoice_id,))
    invoice = cursor.fetchone()
    conn.close()
    return invoice
