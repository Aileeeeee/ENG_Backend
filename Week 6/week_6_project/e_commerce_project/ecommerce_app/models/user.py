# Import libraries
from ecommerce_app import db
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime

# Declare User class
class User:
    # Set database table name 
    __tablename__ = 'users'

    # Define attributes
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(256), nullable=False)
    first_name = db.Column(db.String(80),nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    phone = db.Column(db.String(20))
    address = db.Column(db.Text)
    role = db.Column(db.String(20), nullable=False, default='customer')
    is_active = db.Column(db.Boolean, default=True, nullable=False)
    created_at = db.Column(db.Datetime,default=datetime.utc)
    updated_at = db.Column(db.Datetime, default=datetime.utcnow,onupdate=datatime.utcnow)

    # Defining relationships
    orders = db.relationship('Order', back_populates='user', lazy='dynamic')

    cart = db.relationship('Cart', back_populates='user',uselist=False)

    recommendations = db.relationship('Recommendation', back_populates='user', lazy='dynamic')

    reviews= db.relationship('Review', back_populates='user',lazy='dynamic')


    # Defining methods
    def set_password(self,password):
        self.password_hash = generate_password_hash(password)


    def check_password(self,password):
        return check_password_hash(self.password_hash,password)
    
    def to_dict(self):
        return{
            'id': self.id,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'phone': self.phone,
            'address': self.address,
            'role': self.role,
            'is_active': self.is_active,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }
    

    def __repr__(self):
        return f'<User {self.email} ({self.role}>)'


        


