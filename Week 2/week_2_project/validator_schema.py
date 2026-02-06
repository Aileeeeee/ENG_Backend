# Import libaries
from marshmallow import Schema,fields,validate,validates,ValidationError

@validates('isbn')
def validate_isbn(self, value):
    # Replace hyphens with empty spaces 
    digits_only = value.replace('-', '')
    
    # Check that it contains only digits
    if not digits_only.isdigit():
        raise ValidationError("ISBN must contain only digits (hyphens allowed).")
    
    # Check that length is exactly 13
    if len(digits_only) != 13:
        raise ValidationError("ISBN must be exactly 13 digits long.")


class BookSchema(Schema):
    book_id = fields.Int(dump_only=True)
    title = fields.Str(required=True,validate=validate.Length(max = 200))
    author = fields.Str(required=True,validate=validate.Length(max = 200))
    isbn = fields.Str(required=True)
    year = fields.Int(required=True,validate=validate.Range(min=1000,max=2100))


# Checking if isbn exist
def isbn_exists(isbn,books,exclude_id = None):

    # Skip id of book to be updated
    for i, book in enumerate(books):
        if exclude_id != None and i == exclude_id:
            continue 
        
        if book['isbn'] == isbn:
            return True
    

    return False