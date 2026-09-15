from bank_account import BankAccount


def main():
    print("================================")
    print("       OOP BANK ACCOUNT")
    print("================================")

    name = input("Enter account holder name: ")
    account_number = input("Enter account number: ")

    account = BankAccount(name, account_number, 5000)

    while True:
        print("\n----------- MENU -----------")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Show Transaction History")
        print("5. Exit")
        print("----------------------------")

        choice = input("Enter your choice: ")

        if choice == "1":
            account.check_balance()

        elif choice == "2":
            try:
                amount = float(input("Enter deposit amount: "))
                account.deposit(amount)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "3":
            try:
                amount = float(input("Enter withdrawal amount: "))
                account.withdraw(amount)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "4":
            account.show_transactions()

        elif choice == "5":
            print("\nThank you for using OOP Bank Account!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()