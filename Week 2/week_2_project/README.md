#  RESTful Book Library API

A simple RESTful API built with Flask for managing a book collection.  
This project demonstrates CRUD operations using in-memory storage.

---

## Features

- List all books
- Retrieve a specific book by ID
- Add a new book
- Update an existing book
- Delete a book
- Input validation
- Proper HTTP status codes
- JSON-based responses

---

## Tech Stack

- Python
- Flask
- In-memory data storage (Python list)

---

## API Endpoints

### Home
GET /

Returns a welcome message.

---

### Get all books
GET /books


**Response**
``
{
  "No_of_books_available": 10,
  "books": []
}

### Get a specific book
GET /books/<book_id>

**Response**
``{
  "book_id": 1,
  "title": "Atomic Habits",
  "author": "James Clear",
  "ISBN": "978-0-7352-1129-2",
  "year": 2018
}``

### Add a new book
POST /books

**Request Body**
``{
  "title": "Book Title",
  "author": "Author Name",
  "ISBN": "123-456789",
  "year": 2024
}``
**Response**
``
{
  "message": "Book created successfully."
}``

### Update a book
PUT /books/<book_id>

**Request Body**
``{
  "title": "Updated Title",
  "author": "Updated Author",
  "ISBN": "987-654321",
  "year": 2023
}``

### Delete a book
DELETE /books/<book_id>

**Response**
``{
  "message": "Book deleted successfully"
}``

## How to Run the Project

Install dependencies
``pip install flask``

Run the application
``python app.py``

Access the API at:
``http://127.0.0.1:5000``
