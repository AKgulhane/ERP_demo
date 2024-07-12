# payment_service.py
# This module provides functions to handle customer payment operations in the ERP system.
# Functions include recording a customer payment and updating the accounts receivable.
# It interacts with the accounts receivable and general ledger models.

from models.accounts_receivable import get_accounts_receivable, create_accounts_receivable
from models.general_ledger import create_gl_entry


def record_customer_payment(customer_id, amount):
    payment_date = datetime.now().date()

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''UPDATE AccountsReceivable
                      SET AmountDue = AmountDue - ?, Status = CASE WHEN AmountDue - ? <= 0 THEN 'Paid' ELSE 'Open' END
                      WHERE CustomerID = ? AND Status = 'Open' ''', (amount, amount, customer_id))
    conn.commit()
    conn.close()

    # Add journal entries to the general ledger
    create_gl_entry(payment_date, 5, amount, 0, 'Cash')
    create_gl_entry(payment_date, 6, 0, amount, 'Accounts Receivable')
