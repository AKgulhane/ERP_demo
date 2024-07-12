# general_ledger.py
# This module provides functions to interact with the GeneralLedger table in the database.
# Functions include creating a new general ledger entry and retrieving general ledger entries by entry ID.

from db.db_connection import get_db_connection

def create_gl_entry(transaction_date, account_id, debit, credit, description):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO GeneralLedger (TransactionDate, AccountID, Debit, Credit, Description)
                      VALUES (?, ?, ?, ?, ?)''', (transaction_date, account_id, debit, credit, description))
    conn.commit()
    conn.close()

def get_gl_entry(entry_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM GeneralLedger WHERE EntryID = ?', (entry_id,))
    entry = cursor.fetchone()
    conn.close()
    return entry
