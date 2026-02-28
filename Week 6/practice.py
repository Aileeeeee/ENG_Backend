"""
EXERCISE 1: Write a function
=============================

Write a function called validate_email that:
  - Takes one parameter: email
  - Returns True if email contains "@"
  - Returns False otherwise

def validate_email(email):
    # Your code here
    pass

Test it:
  validate_email("alice@example.com")  → True
  validate_email("notanemail")         → False
"""
def validate_email(email):
    if "@" in email:
        return True
    else:
        return False

print(validate_email("notanemail"))



"""
EXERCISE 2: Work with dictionaries
===================================

Create a function called create_book that:
  - Takes parameters: title, author, year
  - Returns a dictionary with these keys plus an "id" of 1

def create_book(title, author, year):
    # Your code here
    pass

Test:
  create_book("1984", "Orwell", 1949)
  → {"id": 1, "title": "1984", "author": "Orwell", "year": 1949}
"""

def create_book(title,author,year):
    book = {
        'id': 1,
        'title': title,
        'author': author,
        'year': year
    }
    return book

print(create_book("1984", "Orwell", 1949))

"""
EXERCISE 3: Work with lists
============================

Create a function called get_user_names that:
  - Takes a list of user dictionaries
  - Returns a list of just the usernames

users = [
    {"id": 1, "username": "alice"},
    {"id": 2, "username": "bob"}
]

def get_user_names(users):
    # Your code here
    pass

Test:
  get_user_names(users) → ["alice", "bob"]
"""
users = [
    {"id": 1, "username": "alice"},
    {"id": 2, "username": "bob"}
]
def get_usernames(users):

    usernames = [book['username'] for book in users]

    return usernames

print(get_usernames(users))