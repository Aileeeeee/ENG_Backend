# Book Library API

A simple Flask REST API for managing a book library.
The API allows users to create, read, update, and delete books stored in a SQLite database.

## Features

- Create a new book

- Get all books

- Get a single book by ID

- Update a book (partial updates allowed)

- Delete a book

- Input validation using Marshmallow

- SQLite database with SQLAlchemy

## Tech Stack

- Python

- Flask

- Flask-SQLAlchemy

- Marshmallow

- SQLite

- Pytest (for testing)

## Project Structure

project/
├── app.py
├── extensions.py
├── models.py
├── validate_schema.py
├── test.py
└── books.db

## How to Run the App

**Install dependencies:** 

`pip install flask flask-sqlalchemy marshmallow pytest`


**Start the server:**

`python app.py`


The API will run on:

http://127.0.0.1:5000

## API Endpoints
Method	Endpoint	Description
GET	    /books	   Get all books
GET	   /books/<id> Get a specific book
POST  /books	Create a new book
PUT	 /books/<id>	Update a book
DELETE	/books/<id>	Delete a book

## Run Tests
`pytest`