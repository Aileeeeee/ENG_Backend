# Import libraries
from marshmallow import Schema, fields, validate,validates, ValidationError
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from models import BookModel
from models import db



class Bookschema(SQLAlchemySchema):
    class Meta:
       model = BookModel
       load_instance = True 
       sqla_session = db.session

    
    # Define fields and their validation
    id = auto_field(dump_only=True)   
    title = auto_field(required=True)
    author = auto_field(required=True)
    isbn = auto_field(required=True)
    year = auto_field(required=True)


    # Custom validation for ISBN
    @validates('isbn')
    def validate_isbn(self, value):
        digits_only = value.replace('-', '')
        if not digits_only.isdigit():
            raise ValidationError("ISBN must contain only digits (hyphens allowed).")
        if len(digits_only) != 13:
            raise ValidationError("ISBN must be exactly 13 digits long.")

    # Custom validation for year
    @validates('year')
    def validate_year(self, value):
        if value < 1000 or value > 2100:
            raise ValidationError("Year must be between 1000 and 2100")