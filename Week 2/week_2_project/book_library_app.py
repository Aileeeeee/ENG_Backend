from flask import Flask,jsonify,request

from validator_schema import BookSchema,isbn_exists


book_lib = Flask(__name__)
book_lib.json.sort_keys = False

books = [
    {
        "book_id": 1,
        "title": "Atomic Habits",
        "author": "James Clear",
        "isbn": "978-0-7352-1129-2",
        "year": 2018
    },
    {
        "book_id": 2,
        "title": "The 7 Habits of Highly Effective People",
        "author": "Stephen R. Covey",
        "isbn": "978-1-982-13727-3",
        "year": 1989
    },
    {
        "book_id": 3,
        "title": "Think and Grow Rich",
        "author": "Napoleon Hill",
        "isbn": "978-1-58542-433-7",
        "year": 1937
    },
    {
        "book_id": 4,
        "title": "The Power of Now",
        "author": "Eckhart Tolle",
        "isbn": "978-1-57731-152-2",
        "year": 1997
    },
    {
        "book_id": 5,
        "title": "How to Win Friends and Influence People",
        "author": "Dale Carnegie",
        "isbn": "978-0-671-02703-2",
        "year": 1936
    },
    {
        "book_id": 6,
        "title": "Man's Search for Meaning",
        "author": "Viktor E. Frankl",
        "isbn": "978-0-8070-1427-1",
        "year": 1946
    },
    {
        "book_id": 7,
        "title": "The Subtle Art of Not Giving a F*ck",
        "author": "Mark Manson",
        "isbn": "978-0-06-245771-4",
        "year": 2016
    },
    {
        "book_id": 8,
        "title": "Mindset: The New Psychology of Success",
        "author": "Carol S. Dweck",
        "isbn": "978-0-345-47232-8",
        "year": 2006
    },
    {
        "book_id": 9,
        "title": "The Four Agreements",
        "author": "Don Miguel Ruiz",
        "isbn": "978-1-878424-31-9",
        "year": 1997
    },
    {
        "book_id": 10,
        "title": "Can't Hurt Me",
        "author": "David Goggins",
        "isbn": "978-1-544-51223-7",
        "year": 2018
    }
    ]

#Setting next book id
next_book_id = 11

# Display endpoints
@book_lib.route('/')
def home_page():
    return jsonify({'message':'Welcome to the Flask application book library app',
                   'endpoints':{'GET /books' : 'List all books',
                                'GET /books/:id' : 'Get a specific book',
                                'POST /books' : 'Add a new book (title, author, ISBN, year)',
                                'PUT /books/:id' : 'Update a book',
                                'DELETE /books/:id': 'Delete a book'}
                }),200

# Get all books
@book_lib.route('/books' ,methods=['GET'])
def get_all_books():
    return jsonify({'no_of_books_available': len(books),
                        'books': books}),200

# Get specific book
@book_lib.route('/books/<int:book_id>', methods=['GET'])
def specific_book(book_id):
    for book in books:
        if book['book_id'] == book_id:
            return jsonify(book),200
        
    else:
        return jsonify({"error":f"Book with book_id '{book_id}' not found"}),404

# Create new book
@book_lib.route('/books',methods=['POST'])
def create_book():
    global next_book_id
    data = request.get_json()

    schema = BookSchema()

    # Validate input
    try:
        new_book_data = schema.load(data)
    except Exception as err:
        return jsonify({'error':str(err)}),400
    
    # Check if isbn exists
    if isbn_exists(new_book_data['isbn'],books):
        return jsonify({'error':'A book with this isbn already exist.',
                        'isbn':new_book_data['isbn']}),409
    
    # Add new book to book list
    new_book_data['book_id'] = next_book_id
    next_book_id += 1

    books.append(new_book_data)

    return jsonify({'message':'New book successfully created',
                    'new_book':new_book_data}),201

@book_lib.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    # Find the book by book_id inline
    book = None
    for b in books:
        if b['book_id'] == book_id:
            book = b
            break
    
    if book is None:
        return jsonify({'error': 'Book not found'}), 404

    # Get request JSON
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Request body must be JSON'}), 400

    # Validate input
    schema = BookSchema(partial=True)
    try:
        validated_data = schema.load(data)
        if len(validated_data) == 0:
            return jsonify({'error':'At least one field is required to update data.'}), 400
    except Exception as err:
        return jsonify({'error': str(err)}),400

    # Check duplicate ISBN
    if 'isbn' in validated_data:
        if isbn_exists(validated_data['isbn'], books, exclude_id=book_id):
            return jsonify({
                'error': 'A book with this ISBN already exists.',
                'isbn': validated_data['isbn']
            }), 409

    # Update book fields
    for key in validated_data:
        book[key] = validated_data[key]

    return jsonify(book), 200


# Delete book           
@book_lib.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    for book in books:
        if book['book_id'] == book_id:
            books.remove(book)
            return jsonify({'message':'Book deleted successfully'}),200
    
    else:
         return jsonify({
            "success": False,
            "error": "Book not found!",
        }), 404


if __name__ == '__main__':
    book_lib.run(debug=True, host='0.0.0.0',port=5000)
    
