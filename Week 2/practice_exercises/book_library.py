"""
Week 2 Project: RESTful Book Library API
Build a CRUD API for managing a book collection

Requirements:
● GET /books - List all books
● GET /books/:id - Get a specific book
● POST /books - Add a new book (title, author, ISBN, year)
● PUT /books/:id - Update a book
● DELETE /books/:id - Delete a book
● In-memory storage (Python list/dictionary)
● Proper HTTP status codes
● Input validation
● Error handling
"""

#   Import libraries
from flask import Flask, jsonify,request

app = Flask(__name__)

books = [
    {
        "book_id": 1,
        "title": "Atomic Habits",
        "author": "James Clear",
        "ISBN": "978-0-7352-1129-2",
        "year": 2018
    },
    {
        "book_id": 2,
        "title": "The 7 Habits of Highly Effective People",
        "author": "Stephen R. Covey",
        "ISBN": "978-1-982-13727-3",
        "year": 1989
    },
    {
        "book_id": 3,
        "title": "Think and Grow Rich",
        "author": "Napoleon Hill",
        "ISBN": "978-1-58542-433-7",
        "year": 1937
    },
    {
        "book_id": 4,
        "title": "The Power of Now",
        "author": "Eckhart Tolle",
        "ISBN": "978-1-57731-152-2",
        "year": 1997
    },
    {
        "book_id": 5,
        "title": "How to Win Friends and Influence People",
        "author": "Dale Carnegie",
        "ISBN": "978-0-671-02703-2",
        "year": 1936
    },
    {
        "book_id": 6,
        "title": "Man's Search for Meaning",
        "author": "Viktor E. Frankl",
        "ISBN": "978-0-8070-1427-1",
        "year": 1946
    },
    {
        "book_id": 7,
        "title": "The Subtle Art of Not Giving a F*ck",
        "author": "Mark Manson",
        "ISBN": "978-0-06-245771-4",
        "year": 2016
    },
    {
        "book_id": 8,
        "title": "Mindset: The New Psychology of Success",
        "author": "Carol S. Dweck",
        "ISBN": "978-0-345-47232-8",
        "year": 2006
    },
    {
        "book_id": 9,
        "title": "The Four Agreements",
        "author": "Don Miguel Ruiz",
        "ISBN": "978-1-878424-31-9",
        "year": 1997
    },
    {
        "book_id": 10,
        "title": "Can't Hurt Me",
        "author": "David Goggins",
        "ISBN": "978-1-544-51223-7",
        "year": 2018
    }
    ]

@app.route('/')
@app.route('/home')
def home_page():
    return jsonify({'message': 'Welcome to my Flask Application Book Library'})


# Get all books
@app.route('/books', methods=["GET"])
def all_books():
    if books:
        return jsonify({'No_of_books_available':len(books),"books":books}),200
    else:
        return jsonify({"error":"Resource not found"}),404
    
# Get specific book
@app.route('/books/<int:book_id>', methods=['GET'])
def specific_book(book_id):
    for book in books:
        if book['book_id'] == book_id:
            return jsonify(book),200
        
    else:
        return jsonify({"error":f"Book with book_id {book_id} not found"}),404

# Create new book
@app.route('/books', methods=['POST'])
def add_new_book():
    data= request.get_json()

    # Validate user input 
    required_field = ['title','author','ISBN','year']
    missing_field = [field for field in required_field if field not in data]

    if missing_field:
        return jsonify({
            "success": False,
            "error": "Validation Error",
            "missing_fields": missing_field
        }), 400
    
    new_book = {"book_id": len(books) + 1,
        "title": data['title'],
        "author": data['author'],
        "ISBN": data['ISBN'],
        "year": data['year']}

    books.append(new_book)
    return jsonify({'message': 'Book created successfully.'})


# Update book
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.get_json()

    for book in books:
        if book['book_id'] == book_id:
            
            book["title"] = data['title']
            book["author"] = data['author']
            book["ISBN"] = data['ISBN']
            book["year"] = data['year']
            
            return jsonify({'message': 'Book updated successfully'}),200
    else:
         return jsonify({
            "success": False,
            "error": "Book not found!",
        }), 400

# Delete book           
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    for book in books:
        if book['book_id'] == book_id:
            books.remove(book)
            return jsonify({'message':'Book deleted successfully'})
    
    else:
         return jsonify({
            "success": False,
            "error": "Book not found!",
        }), 400

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=5000)

