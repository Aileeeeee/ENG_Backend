# Import libraries
from flask import Flask,request,jsonify
from extensions import db
from models import BookModel
from validate_schema import Bookschema

# Initialize Flask application and Database
book_lib = Flask(__name__)
book_lib.json_sort_keys = False

# Configure SQLite Database
book_lib.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
book_lib.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

# Initialize SQLALCHEMY
db.init_app(book_lib)

# Create tables if they don't exist
with book_lib.app_context():
    db.create_all()


# Display endpoints
@book_lib.route('/')
def home_page():
    return jsonify({
        'message': 'Welcome to the Flask application book library app',
        'endpoints': {
            'GET /books': 'List all books',
            'GET /books/:id': 'Get a specific book',
            'POST /books': 'Add a new book (title, author, ISBN, year)',
            'PUT /books/:id': 'Update a book',
            'DELETE /books/:id': 'Delete a book'
        }
    }), 200


# Get all books
@book_lib.route('/books', methods=['GET'])
def get_all_books():

    # Fetch all books from database
    books = BookModel.query.all()
    schema = Bookschema(many=True)
    return jsonify({
        'no_of_books_available': len(books),
        'books':schema.dump(books)
    }),200

# Get a specific book
@book_lib.route('/books/<int:book_id>',methods=['GET'])
def specific_book(book_id):
    book = BookModel.query.get(book_id)

    if not book:
         return jsonify({"error": f"Book with book_id '{book_id}' not found"}), 404
    

    schema = Bookschema()
    return jsonify(schema.dump(book)),200


# Create new book
@book_lib.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()
    
    if not data:
        return jsonify({'error': "Request data must be in JSON format"}),400
    
    schema = Bookschema()

    # Validate request data and create book object
    try:
        book = schema.load(data, session =db.session)
    except Exception as err:
            return jsonify({'error':str(err)}),400


    # Check if ISBN exists
    if BookModel.query.filter_by(isbn=book.isbn).first():
        return jsonify({
            'error':'A book with this ISBN already exists',
            'isbn': book.isbn
        }),409
    
    db.session.add(book)
    db.session.commit()

    return jsonify ({
        'message': 'New book successfully created',
        'new_book': schema.dump(book)
    }),201

# Update a book entry (partial allowed)
@book_lib.route('/books/<int:book_id>',methods = ['PUT'])
def update_book(book_id):
    book = BookModel.query.get(book_id)
    
    if not book:
        return jsonify({'error': 'Book not found'}),404

    data = request.get_json()
    if not data:
        return jsonify({'error': 'Request body must be in JSON'}),400
    
    
    schema = Bookschema(partial=True)
    try:
        updated_book = schema.load(data, instance=book, session=db.session)
    except Exception as err:
        return jsonify({'error':str(err)}),400
    
    # Check for duplicate ISBN
    if 'isbn' in data:
        existing = BookModel.query.filter_by(isbn=data['isbn']).first()
        if existing and existing.id != book.id:
            return jsonify({
                'error': 'A book with this ISBN already exists.',
                'isbn': data['isbn']
            }),409


    db.session.commit()
    return jsonify(schema.dump(book)),200


# Delete book
@book_lib.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = BookModel.query.get(book_id)
    if not book:
        return jsonify({'error': 'Book not found'}), 404
    
    db.session.delete(book)
    db.session.commit()
    return jsonify({'message': 'Book deleted succesfully'}),200


if __name__ == '__main__':
    book_lib.run(debug=True, host='0.0.0.0', port=5000)