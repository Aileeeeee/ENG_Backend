"""Exercise 3: Shopping List Manager
Challenge:
Create a shopping list program with multiple features.
Requirements:

Start with an empty shopping list
Create a menu with these options:

Add item to list
Remove item from list
View all items
Count total items
Sort list alphabetically
Clear entire list
Exit program


Use a function for each menu option
Keep the program running until the user chooses to exit
Use if statements to handle menu choices

Hints:

Use a while loop to keep program running
Create separate functions like add_item(), remove_item(), etc.
Each function should take the list as a parameter
Remember to return the modified list

Sample Interaction:
=== Shopping List Manager ===
1. Add item
2. Remove item
3. View list
4. Exit

Choice: 1
Item to add: Milk
Added!

Choice: 3
Your list: ['Milk']"""

# Define a variable to store an empty shopping list 
shopping_list = []

# Define function to add item to shopping list 
def add_item(shopping_list):
    item = input(f"Item to add: ").title()
    shopping_list.append(item)
    print(f"{item} added!\n")
    return shopping_list

# Define function to remove item from shopping list 
def remove_item(shopping_list):
    item = input(f"Item to remove: \n").title()

    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} removed!\n")
    else:
        print(f"{item} not found in shopping list.\n")
    return shopping_list 

# Define function to view items in shopping list 
def view_items(shopping_item):
    if shopping_list:
        print(f"Your list: {shopping_item}\n")
    else:
        print("\nYou have no items in your shopping list.")

while True:
    print("==== Shopping List Manager ====")
    print("1. Add item")
    print("2. Remove item")
    print("3. View items")
    print("4. Exit")

    choice = input("Choice: ")

    if choice == "1":
        add_item(shopping_list)
    elif choice == "2":
        remove_item(shopping_list)
    elif choice == "3":
        view_items(shopping_list)
    elif choice == "4":
        print("Exiting shopping list manager.......")
        break
    else:
        print("Invalid option! Choose an option from the list.\n")