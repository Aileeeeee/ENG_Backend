from ecommerce_app import db
from datetime import datetime

class Cart(db.Model):
    __tablename__ = "carts"

    id = db.Column(db.Integer, primary_key=True)
    
    # Foreign key: links to users table
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), unique=True, nullable=False)
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # --- Relationships ---
    user = db.relationship("User", back_populates="cart")
    items = db.relationship("CartItem", back_populates="cart", cascade="all, delete-orphan")

    @property
    def total_price(self):
        return sum(item.subtotal for item in self.items)

    @property
    def total_items(self):
        return sum(item.quantity for item in self.items)

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "items": [item.to_dict() for item in self.items],
            "total_items": self.total_items,
            "total_price": float(self.total_price),
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }


class CartItem(db.Model):
    
    __tablename__ = "cart_items"

    id = db.Column(db.Integer, primary_key=True)
    
    # Foreign keys
    cart_id = db.Column(db.Integer, db.ForeignKey("carts.id"), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)
    

    quantity = db.Column(db.Integer, nullable=False, default=1)
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Prevent no duplicate products in the same cart
    __table_args__ = (
        db.UniqueConstraint("cart_id", "product_id", name="unique_cart_product"),
    )

    # Relationships
    cart = db.relationship("Cart", back_populates="items")
    product = db.relationship("Product", back_populates="cart_items")

    @property
    def subtotal(self):
        return float(self.product.price) * self.quantity

    def to_dict(self):
        return {
            "id": self.id,
            "cart_id": self.cart_id,
            "product": self.product.to_dict() if self.product else None,
            "quantity": self.quantity,
            "unit_price": float(self.product.price) if self.product else 0,
            "subtotal": self.subtotal,
        }
