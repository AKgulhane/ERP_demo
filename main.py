from services.sales_service.py import record_sale
from services.purchase_service.py import record_purchase
from services.payment_service.py import record_customer_payment
from datetime import datetime


# Example Usage
def main():
    # Create a sale
    customer_id = 1
    sales_person_id = 1
    products_sold = [(1, 2), (2, 1)]  # (product_id, quantity)
    total_amount = 300.0
    currency = 'USD'
    payment_method = 'Credit Card'

    sale_id = record_sale(customer_id, sales_person_id, products_sold, total_amount, currency, payment_method)
    print(f'Sale recorded with ID: {sale_id}')

    # Record a purchase
    vendor_id = 1
    products_purchased = [(1, 10, 20.0), (2, 5, 15.0)]  # (product_id, quantity, cost_price)
    total_amount = 350.0

    invoice_id = record_purchase(vendor_id, products_purchased, total_amount)
    print(f'Purchase recorded with Invoice ID: {invoice_id}')

    # Record a customer payment
    customer_id = 1
    amount = 150.0

    record_customer_payment(customer_id, amount)
    print(f'Customer payment of {amount} recorded for Customer ID: {customer_id}')


if __name__ == '__main__':
    main()
