# Import libaries
from ecommerce_app import db
from datetime import datetime

# Define class `Category`
class Category(db.Model):
    __tablename__ = 'categories'

    # Define columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String,nullable=False,unique=True)
    description = db.Column(db.Text)
    created_at = db.Column(db.Datetime, default=datetime.utcnow)

    parent_id = db.Column(db.Integer,db.ForeignKey('categories.id',nullable=True))

    # Define relationships
    products = db.relationship('Product',back_populates='category', lazy='dynamic')
    subcategories = db.relationship('Category',backref=db.backref('parent',remote_side=[id],lazy='dynamic'))

    def to_dict(self):
        return{
            'id':self.id,
            'name': self.name,
            'description':self.description,
            'parent_id':self.parent_id
        }
    

# Define class `Product`
class Product(db.Model):
    __tablename__ = 'products'

    # Define columns
    id = db.Columns(db.Integer, primary_key= True)
    name = db.Column(db.String(200),nullable=False)
    description = db.Column(db.Text)
    
    storage_instructions = db.Column(db.Text)
    warnings = db.Colum(db.Text)
    
    # Pricing columns
    price = db.Column(db.Numeric(10,2), nullable=False)
    

    # Inventory Columns
    stock_quantity = db.Column(db.Integer,default=0,nullable=False)
    low_stock_threshold = db.Column(db.Integer,default=12)
    unit = db.Column(db.String(50),default='unit')

    image_url = db.Column(db.String(500))
    is_active = db.Column(db.Boolean,default=True,nullable=False)
    created_at = db.Column(db.Datetime,default=datetime.utcnow,nullable=False)
    updated_at = db.Column(db.Datetime,default=datetime.utcnow,onupdate=datetime.utcnow)

    # Define foreign key
    category_id =db.Column(db.Integer,db.ForeignKey('categories.id'),nullable=True)

    # Define relationships 
    category = db.relationship('Category',back_populates='products')
    reviews = db.relationship('Review',back_populates='product',lazy='dynamic')
    cart_items = db.relationship('CartItem',back_populates='product')
    order_items = db.relationship('OrderItem',back_populates='product')

    # Calculate average star rating from all reviews
    @property
    def average_rating(self):
        reviews = self.reviews.all()
        if not reviews:
            return 0 
        total = sum(r.rating for r in reviews)
        return round(total / len(reviews),1)
    
    # Check if products have stock available
    @property
    def is_in_stock(self):
        return self.stock_quantity > 0
    
    # Check is stock is below alert threshold
    @property
    def is_low_stock(self):
        return 0 < self.stock_quantity <= self.low_stock_threshold
    
    # Convert to dictionary for JSON response
    def to_dict(self, include_reviews=False):
        data = {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "storage_instructions": self.storage_instructions,
            "warnings": self.warnings,
            "price": float(self.price),
            "stock_quantity": self.stock_quantity,
            "unit": self.unit,
            "is_in_stock": self.is_in_stock,
            "is_low_stock": self.is_low_stock,
            "image_url": self.image_url,
            "is_active": self.is_active,
            "average_rating": self.average_rating,
            "review_count": self.reviews.count(),
            "category": self.category.to_dict() if self.category else None,
            "created_at": self.created_at.isoformat() if self.created_at else None,
        }
        
        if include_reviews:
            data["reviews"] = [r.to_dict() for r in self.reviews.limit(10).all()]
        
        return data

    def __repr__(self):
        return f"<Product {self.name} (${self.price})>"

# Define `Review` class
class Review:

    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)
    
    # Foreign Keys
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    
    # Review Content
    rating = db.Column(db.Integer, nullable=False)  # 1-5 stars
    title = db.Column(db.String(200))
    body = db.Column(db.Text)
    is_verified_purchase = db.Column(db.Boolean, default=False)
    is_approved = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    product = db.relationship("Product", back_populates="reviews")
    user = db.relationship("User", back_populates="reviews")

    # Set constraint to prevent one user from reviewing a product twice
    __table_args__ = (
        db.UniqueConstraint("product_id", "user_id", name="unique_user_product_review"),
    )

    def to_dict(self):
        return {
            "id": self.id,
            "product_id": self.product_id,
            "user_id": self.user_id,
            "user_name": f"{self.user.first_name} {self.user.last_name[0]}." if self.user else "Anonymous",
            "rating": self.rating,
            "title": self.title,
            "body": self.body,
            "is_verified_purchase": self.is_verified_purchase,
            "created_at": self.created_at.isoformat() if self.created_at else None,
        }



