# 🏦 OOP Bank Account

A simple Bank Account Management System built using Python Object-Oriented Programming (OOP) and Pandas.

## 📌 Project Overview

This project simulates basic banking operations such as creating a bank account, depositing money, withdrawing money, checking the account balance, and viewing transaction history.

The project also stores transaction data in a CSV file and uses Pandas to perform data analysis.

## 🎯 Objectives

- Understand Object-Oriented Programming in Python.
- Implement a Bank Account using classes and methods.
- Perform deposit and withdrawal operations.
- Maintain transaction history.
- Store banking data in a CSV file.
- Analyze transaction data using Pandas.
- Handle invalid user input and banking errors.

## ✨ Features

- Create a bank account
- Check account balance
- Deposit money
- Withdraw money
- Prevent withdrawals when balance is insufficient
- Validate invalid amounts
- Display transaction history
- Automatically save transactions to CSV
- Perform transaction analysis using Pandas
- Analyze deposits and withdrawals
- Category-wise transaction analysis

## 🛠️ Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- Pandas
- CSV

## 📂 Project Structure

OOP-Bank-Account/
│
├── bank_account.py
├── main.py
├── transactions.csv
├── analysis.py
└── README.md

## 🧠 OOP Concepts Used

### Class

The `BankAccount` class represents a bank account.

### Constructor

The `__init__()` method initializes the account holder, account number, balance, and transaction history.

### Methods

Methods such as `deposit()`, `withdraw()`, `check_balance()`, and `show_transactions()` perform banking operations.

### Encapsulation

Account information and transaction data are maintained inside the `BankAccount` object.

## 📊 Pandas Analysis

The `analysis.py` program reads `transactions.csv` using Pandas and calculates:

- Total number of transactions
- Total deposits
- Total withdrawals
- Highest transaction
- Average transaction
- Deposit and withdrawal counts
- Category-wise transaction amounts
- Highest deposit
- Highest withdrawal

## ▶️ How to Run

### 1. Install Pandas

pip install pandas

### 2. Run the Bank Account Program

python main.py

### 3. Run Transaction Analysis

python analysis.py

## 💻 Sample Banking Operations

----------- MENU -----------
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Show Transaction History
5. Exit
----------------------------
Enter your choice:

## 📈 Sample Analysis

--- Summary ---
Total Transactions : 11
Total Deposits     : ₹16000.00
Total Withdrawals  : ₹8200.00
Highest Transaction: ₹5000.00
Average Transaction: ₹2200.00

## 🔒 Error Handling

The application handles:

- Invalid menu choices
- Negative or zero deposit amounts
- Negative or zero withdrawal amounts
- Withdrawals greater than the available balance
- Invalid numeric input

## 👩‍💻 Author

Dhwani

## 📄 License

This project is created for educational purposes.