# sales_service.py
# This module provides functions to handle sales operations in the ERP system.
# Functions include recording a sale and retrieving sale details.
# It interacts with the sales, inventory, and general ledger models.

from models.sales import create_sale, get_sale
from models.inventory import update_inventory
from models.general_ledger import create_gl_entry


def record_sale(customer_id, sales_person_id, products_sold, total_amount, currency, payment_method):
    sale_date = datetime.now().date()

    sale_id = create_sale(customer_id, sales_person_id, sale_date, total_amount, currency, payment_method, 'Completed')

    for product_id, quantity_sold in products_sold:
        update_inventory(product_id, -quantity_sold, None, None)

    # Add journal entries to the general ledger
    create_gl_entry(sale_date, 1, total_amount, 0, 'Sales Revenue')
    create_gl_entry(sale_date, 2, 0, total_amount, 'Accounts Receivable')

    return sale_id


def get_sale_details(sale_id):
    return get_sale(sale_id)
