# <b>📊 Personal Budget Tracker
A simple and effective tool to manage your personal finances! Keep track of your income and expenses, view reports, and export data seamlessly. 🧾✨

# <b>🚀 Features <br>
➕ Add Transactions: Record your income and expenses with categories like groceries, salary, and more.<br><br>
📊 View Transactions: Display all transactions in a user-friendly table format.<br><br>
❌ Delete Transactions: Remove incorrect or unnecessary entries.<br><br>
📁 Export to CSV: Generate reports to analyze your spending habits.<br><br>
🗄️ Database Storage: All data is safely stored in an SQLite database.<br><br>
# <b>🛠️ Installation :</b>
Clone or Download the Project:

git clone <b>https://github.com/rutujakale111/Personal-Budget-Tracker-Using-Python</b>
cd personal-budget-tracker
Set Up Python:

Ensure Python 3.x is installed. Check with:

python --version
Run the Application:

python main.py

# <b>📋 How to Use 
Launch the app with python main.py.<br><br>
Select an option from the menu:<br><br>
1: Add a transaction 💰<br><br>
2: View all transactions 📝<br><br>
3: Delete a transaction 🗑️<br><br>
4: Export to CSV 📤<br><br>
5: Exit the program 🚪<br><br>

# <b>📦 Folder Structure
personal_budget_tracker/
├── main.py      
├── tracker.py    
├── database.py   
├── budget.db 

# <b>🧪 Example
Adding a Transaction:

Date (YYYY-MM-DD): 2025-01-02
Category: Groceries
Amount: -50
Type (income/expense): expense
Transaction added successfully! ✅

**Viewing Transactions:**

ID   Date       Category    Amount     Type
1    2025-01-02 Groceries   -50.00     expense

Exported CSV File:

ID,Date,Category,Amount,Type
1,2025-01-02,Groceries,-50.00,expense
