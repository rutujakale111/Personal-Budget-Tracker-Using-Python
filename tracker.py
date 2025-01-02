import csv
from datetime import datetime
from database import add_transaction, get_all_transactions, delete_transaction

def add_new_transaction():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (e.g., groceries, salary): ")
    amount = float(input("Enter amount: "))
    type = input("Enter type (income/expense): ").lower()

    if type not in ['income', 'expense']:
        print("Invalid type. Please enter 'income' or 'expense'.")
        return

    add_transaction(date, category, amount, type)
    print("Transaction added successfully!")

def view_transactions():
    transactions = get_all_transactions()
    print("\nID | Date       | Category       | Amount   | Type")
    print("-- | ---------- | -------------- | -------- | --------")
    for transaction in transactions:
        print(f"{transaction[0]}  | {transaction[1]} | {transaction[2]:<14} | {transaction[3]:<8} | {transaction[4]}")

def delete_existing_transaction():
    transaction_id = int(input("Enter the ID of the transaction to delete: "))
    delete_transaction(transaction_id)
    print("Transaction deleted successfully!")

def export_to_csv():
    transactions = get_all_transactions()
    filename = f"budget_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Date", "Category", "Amount", "Type"])
        writer.writerows(transactions)

    print(f"Data exported to {filename}")