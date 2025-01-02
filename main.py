from tracker import add_new_transaction, view_transactions, delete_existing_transaction, export_to_csv
from database import initialize_database

def main_menu():
    while True:
        print("\nPersonal Budget Tracker")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Delete Transaction")
        print("4. Export Transactions to CSV")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_new_transaction()
        elif choice == '2':
            view_transactions()
        elif choice == '3':
            delete_existing_transaction()
        elif choice == '4':
            export_to_csv()
        elif choice == '5':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    initialize_database()
    main_menu()