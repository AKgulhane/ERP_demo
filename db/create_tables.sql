-- create_tables.sql
-- This script creates the database schema for the ERP system.
-- It includes tables for customers, salespersons, products, sales, inventory, general ledger,
-- accounts payable, accounts receivable, and vendors.
-- Run this script to initialize the database before using the application.

CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(100),
    Address TEXT,
    Email VARCHAR(100)
);

CREATE TABLE SalesPersons (
    SalesPersonID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(100),
    Email VARCHAR(100)
);

CREATE TABLE Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(100),
    Description TEXT,
    Price DECIMAL(10, 2)
);

CREATE TABLE Sales (
    SaleID INT PRIMARY KEY AUTO_INCREMENT,
    CustomerID INT,
    SalesPersonID INT,
    SaleDate DATE,
    TotalAmount DECIMAL(10, 2),
    Currency VARCHAR(3),
    PaymentMethod VARCHAR(50),
    Status ENUM('Pending', 'Completed', 'Cancelled'),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
    FOREIGN KEY (SalesPersonID) REFERENCES SalesPersons(SalesPersonID)
);

CREATE TABLE Inventory (
    InventoryID INT PRIMARY KEY AUTO_INCREMENT,
    ProductID INT,
    Quantity INT,
    CostPrice DECIMAL(10, 2),
    SellingPrice DECIMAL(10, 2),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);

CREATE TABLE GeneralLedger (
    EntryID INT PRIMARY KEY AUTO_INCREMENT,
    TransactionDate DATE,
    AccountID INT,
    Debit DECIMAL(10, 2),
    Credit DECIMAL(10, 2),
    Description TEXT,
    FOREIGN KEY (AccountID) REFERENCES ChartOfAccounts(AccountID)
);

CREATE TABLE ChartOfAccounts (
    AccountID INT PRIMARY KEY AUTO_INCREMENT,
    AccountName VARCHAR(100),
    AccountType ENUM('Asset', 'Liability', 'Equity', 'Revenue', 'Expense')
);

CREATE TABLE AccountsPayable (
    InvoiceID INT PRIMARY KEY AUTO_INCREMENT,
    VendorID INT,
    InvoiceDate DATE,
    DueDate DATE,
    AmountDue DECIMAL(10, 2),
    Status ENUM('Open', 'Paid'),
    FOREIGN KEY (VendorID) REFERENCES Vendors(VendorID)
);

CREATE TABLE AccountsReceivable (
    InvoiceID INT PRIMARY KEY AUTO_INCREMENT,
    CustomerID INT,
    InvoiceDate DATE,
    DueDate DATE,
    AmountDue DECIMAL(10, 2),
    Status ENUM('Open', 'Paid'),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

CREATE TABLE Vendors (
    VendorID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(100),
    Address TEXT,
    Email VARCHAR(100)
);
