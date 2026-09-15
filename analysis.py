import pandas as pd


# Load transaction data
df = pd.read_csv("transactions.csv")

print("\n========================================")
print("       BANK TRANSACTION ANALYSIS")
print("========================================")

# Display all transactions
print("\n--- All Transactions ---")
print(df.to_string(index=False))


# Basic statistics
total_transactions = len(df)

total_deposits = df.loc[
    df["type"] == "Deposit", "amount"
].sum()

total_withdrawals = df.loc[
    df["type"] == "Withdrawal", "amount"
].sum()

highest_transaction = df["amount"].max()

average_transaction = df["amount"].mean()


# Display basic statistics
print("\n--- Summary ---")
print(f"Total Transactions : {total_transactions}")
print(f"Total Deposits     : ₹{total_deposits:.2f}")
print(f"Total Withdrawals  : ₹{total_withdrawals:.2f}")
print(f"Highest Transaction: ₹{highest_transaction:.2f}")
print(f"Average Transaction: ₹{average_transaction:.2f}")


# Deposit vs Withdrawal count
print("\n--- Transaction Count ---")

transaction_counts = df["type"].value_counts()

print(transaction_counts)


# Category-wise analysis
print("\n--- Category-wise Transaction Amount ---")

category_summary = (
    df.groupby("category")["amount"]
    .sum()
    .sort_values(ascending=False)
)

print(category_summary)


# Withdrawal analysis
print("\n--- Withdrawal Analysis ---")

withdrawals = df[df["type"] == "Withdrawal"]

if not withdrawals.empty:
    highest_withdrawal = withdrawals["amount"].max()
    print(f"Highest Withdrawal: ₹{highest_withdrawal:.2f}")

    print("\nWithdrawal Transactions:")
    print(withdrawals.to_string(index=False))


# Deposit analysis
print("\n--- Deposit Analysis ---")

deposits = df[df["type"] == "Deposit"]

if not deposits.empty:
    highest_deposit = deposits["amount"].max()
    print(f"Highest Deposit: ₹{highest_deposit:.2f}")

    print("\nDeposit Transactions:")
    print(deposits.to_string(index=False))


print("\n========================================")
print("       ANALYSIS COMPLETED")
print("========================================")