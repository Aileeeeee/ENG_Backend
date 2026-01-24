"""Exercise 7: Budget Tracker
Challenge:
Create a simple budget tracking program.

Requirements:
Set a monthly budget at the start
Track expenses as a list of tuples: (item_name, cost)
Features:
Add an expense
View all expenses
Calculate total spent
Calculate remaining budget
Find most expensive item
Find cheapest item
Calculate average expense
Check if over budget (with warning message)
Use functions with return statements
Use if/elif/else for budget status messages:
"Great! Under budget"
"Warning! 80% of budget used"
"ALERT! Over budget!"
Hints:
Store budget as a variable
Store expenses as a list of tuples
Use sum() with a loop to calculate total
"""

"""Requirements:
Set a monthly budget at the start
Track expenses as a list of tuples: (item_name, cost)
Features:
Add an expense
View all expenses
Calculate total spent
Calculate remaining budget
Find most expensive item
Find cheapest item
Calculate average expense
Check if over budget (with warning message)
Use functions with return statements
Use if/elif/else for budget status messages:
"Great! Under budget"
"Warning! 80% of budget used"
"ALERT! Over budget!" """

# Set variable to store monthly budget
monthly_budget = float(input("Enter a monthly budget: ₦"))
expenses = []

# Define a function to add a new expense
def add_expense(expenses):
    item_name = input("Enter the name of the expense made: ").title()
    item_cost = float(input(" How much does it cost: ₦"))

    expenses.append((item_name,item_cost))
    return expenses

# Define a function to view all expenses
def view_expenses(expenses): 
    if expenses:
        for index, expense in enumerate(expenses, start=1):
            print(f"{index}. {expense[0]}: ₦{round(expense[1])}")
    else:
        print("No expenses has been made!")
    return expenses

# Define function to calculate total amount spent
def calculate_total(expenses):
    total_amount_spent = 0
    for expense in expenses:
        total_amount_spent += expense[1]
    return total_amount_spent

# Define a function to calculate the remaining budget
def calculate_remaining_budget():
    total_amount_spent = calculate_total(expenses)

    if monthly_budget > total_amount_spent:
        remaining_budget = monthly_budget - total_amount_spent 
        return remaining_budget
    else:
        print("You've exhausted your monthly budget. You have ₦0 left.")
        return 0
        
# Define a function to get the expensive item
def get_expensive_item(expenses):

    if not expenses:
        return None
    
    expensive_item = expenses[0]
    for expense in expenses:
        if expense[1] > expensive_item[1]:
            expensive_item = expense
    return expensive_item

# Define a function to get the cheapest item
def get_cheapest_item(expenses):

    if not expenses:
        return None

    cheapest_item = expenses[0]
    for expense in expenses:
        if expense[1] < cheapest_item[1]:
            cheapest_item = expense
    return cheapest_item

# Define a function to get the average expense
def calculate_average_expense(expenses):
    expense_costs = []

    if expenses:
        for expense in expenses:
            expense_costs.append(expense[1])
        average_expense = sum(expense_costs) / len(expense_costs)
        return average_expense
    else:
        return None
    
# Define function  to check monthly budget limit

def check_budget_limit():
    total_expenses = calculate_total(expenses)
    eighty_percent = 0.8 * monthly_budget

    if total_expenses < monthly_budget and total_expenses < eighty_percent:
        return "Great! Under budget"
    elif total_expenses == eighty_percent:
        return "Warning! 80% of budget used"
    else:
        return "ALERT! Over budget!" 


    
    
    
while True:
    print("\n=== Budget Tracker Menu ===")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Calculate total amount spent")
    print("4. Calculate remaining budget")
    print("5. Get most expensive expense")
    print("6. Get most cheapest expense")
    print("7. Get average expense")
    print("8. Check budget limit")
    print("9. Exit")
    

    choice = input("Choice: ")

    if choice == '1':
        expenses = add_expense(expenses)
        print("Expense added!\n")
    elif choice == '2':
        print("\n==== My Expenses ====")
        view_expenses(expenses)
    elif choice == '3':
        print(f"Total amount spent: ₦{calculate_total(expenses)}")
    elif choice == '4':
        print(f"Remaining budget: ₦{calculate_remaining_budget()}")
    elif choice == '5':
        expensive_item = get_expensive_item(expenses)

        if expensive_item:
            print(f"Most expensive expense: {expensive_item[0]} - (₦{round(expensive_item[1])})")
        else:
            print("No expenses recorded yet.\n")
    elif choice == '6':
        cheapest_item = get_cheapest_item(expenses)

        if cheapest_item:
            print(f"Most cheapest expense: {cheapest_item[0]} - (₦{round(cheapest_item[1])})")
        else:
            print("No expenses recorded yet.\n")
    elif choice == '7':
        average_expense = calculate_average_expense(expenses)

        if average_expense:
            print(f"Average expense: ₦{round(average_expense)}")
        else:
            print("No expenses recorded yet.\n")
    elif choice == '8':
        print(f"Budget limit status: {check_budget_limit()}")
        
    elif choice == '9':
        print("Exiting Budget Tracker. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")    

    
