import csv


class BankAccount:
    def __init__(self, account_holder, account_number, balance=0):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than 0.")
            return

        self.balance += amount

        transaction = {
            "type": "Deposit",
            "amount": amount,
            "balance": self.balance
        }

        self.transactions.append(transaction)

        self.save_transaction("Deposit", amount)

        print(f"₹{amount:.2f} deposited successfully.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than 0.")
            return

        if amount > self.balance:
            print("Insufficient balance.")
            return

        self.balance -= amount

        transaction = {
            "type": "Withdrawal",
            "amount": amount,
            "balance": self.balance
        }

        self.transactions.append(transaction)

        self.save_transaction("Withdrawal", amount)

        print(f"₹{amount:.2f} withdrawn successfully.")

    def check_balance(self):
        print(f"Current balance: ₹{self.balance:.2f}")

    def show_transactions(self):
        if not self.transactions:
            print("No transactions found.")
            return

        print("\nTransaction History")
        print("-" * 40)

        for transaction in self.transactions:
            print(
                f"{transaction['type']}: "
                f"₹{transaction['amount']:.2f} | "
                f"Balance: ₹{transaction['balance']:.2f}"
            )

    def save_transaction(self, transaction_type, amount):
        with open("transactions.csv", "a", newline="") as file:
            writer = csv.writer(file)

            writer.writerow([
                "AUTO",
                self.account_number,
                transaction_type,
                amount,
                self.balance,
                "Banking"
            ])