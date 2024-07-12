# purchase_service.py
# This module provides functions to handle purchase operations in the ERP system.
# Functions include recording a purchase and updating the inventory and accounts payable.
# It interacts with the accounts payable, inventory, and general ledger models.

from models.accounts_payable import create_accounts_payable
from models.inventory import update_inventory
from models.general_ledger import create_gl_entry


def record_purchase(vendor_id, products_purchased, total_amount):
    invoice_date = datetime.now().date()
    due_date = invoice_date.replace(month=invoice_date.month + 1)

    invoice_id = create_accounts_payable(vendor_id, invoice_date, due_date, total_amount, 'Open')

    for product_id, quantity_purchased, cost_price in products_purchased:
        update_inventory(product_id, quantity_purchased, cost_price, cost_price * 1.2)  # Assume 20% markup

    # Add journal entries to the general ledger
    create_gl_entry(invoice_date, 3, total_amount, 0, 'Inventory Purchase')
    create_gl_entry(invoice_date, 4, 0, total_amount, 'Accounts Payable')

    return invoice_id
