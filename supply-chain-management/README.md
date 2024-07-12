# ERP System

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [System Architecture](#system-architecture)
4. [Database Schema](#database-schema)
5. [Installation](#installation)
6. [Usage](#usage)
7. [Modules](#modules)
8. [Contributing](#contributing)
9. [License](#license)

## Introduction

This ERP (Enterprise Resource Planning) system is designed to manage core business processes such as sales, purchases, inventory, customer relations, and financials in an integrated manner. It is intended for use by small to medium-sized businesses, particularly in the automotive industry.

## Features

- Customer management
- Sales management
- Inventory management
- Vendor management
- Purchase management
- Accounts payable and receivable
- General ledger

## System Architecture

The ERP system follows a modular architecture, with each module responsible for a specific aspect of the business process. The architecture diagram below provides a high-level overview of the system.

![image](https://github.com/user-attachments/assets/8aaffa0c-f839-4aaf-b998-8893105049b8)


## Database Schema

The database schema includes tables for customers, salespersons, products, sales, inventory, general ledger, accounts payable, accounts receivable, and vendors. The schema diagram below illustrates the relationships between these tables.


## Installation

### Prerequisites

- Python 3.x
- SQLite3

### Steps

1. Clone the repository:
   ```sh
   git clone https://github.com/AKgulhane/erp-system.git
   cd erp-system
   ```

2. Install the required Python packages:
   ```sh
   pip install -r requirements.txt
   ```

3. Set up the database:
   ```sh
   sqlite3 erp_system.db < db/create_tables.sql
   ```

## Usage

To run the application, execute the `main.py` file. This file includes example usage of the various services provided by the ERP system.

```sh
python main.py
```

The example usage includes:

- Recording a sale
- Recording a purchase
- Recording a customer payment

## Modules

The ERP system consists of the following modules:

### Models

- **Customers:** Manages customer information.
- **Salespersons:** Manages salesperson information.
- **Products:** Manages product information.
- **Sales:** Manages sales transactions.
- **Inventory:** Manages inventory records.
- **General Ledger:** Manages general ledger entries.
- **Accounts Payable:** Manages vendor invoices and payments.
- **Accounts Receivable:** Manages customer invoices and payments.
- **Vendors:** Manages vendor information.

### Services

- **Sales Service:** Handles sales operations, updating inventory and general ledger accordingly.
- **Purchase Service:** Handles purchase operations, updating inventory and accounts payable accordingly.
- **Payment Service:** Handles customer payments, updating accounts receivable and general ledger accordingly.

## Contributing

We welcome contributions to improve this ERP system. Please follow the steps below to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes and commit them (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a new Pull Request.

## License

This project is open.
