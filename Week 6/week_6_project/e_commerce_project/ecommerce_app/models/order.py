from ecommerce_app import db
from datetime import datetime

class Order(db.Model):
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True)

    # Set foreign Key 
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    # Order Status
    # Valid values: pending, confirmed, processing, shipped, delivered, cancelled
    status = db.Column(db.String(20), nullable=False, default="pending")

    # Financial columns
    subtotal = db.Column(db.Numeric(10, 2), nullable=False)
    delivery_fee = db.Column(db.Numeric(10, 2), default=0)
    total_amount = db.Column(db.Numeric(10, 2), nullable=False)

    # Delivery Info 
    delivery_address = db.Column(db.Text, nullable=False)

    # Payment 
    # payment_status: pending, paid, refunded, failed
    payment_status = db.Column(db.String(20), default="pending")
    
    # Notes
    customer_notes = db.Column(db.Text)  # Special instructions from customer
    admin_notes = db.Column(db.Text)     # Internal notes for staff

    # Timestamps 
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Set when was the order shipped / delivered?
    shipped_at = db.Column(db.DateTime)
    delivered_at = db.Column(db.DateTime)

    # Relationships 
    user = db.relationship("User", back_populates="orders")
    order_items = db.relationship("OrderItem", back_populates="order", cascade="all, delete-orphan")

    @property
    def item_count(self):
        return sum(item.quantity for item in self.items)

    def to_dict(self, include_items=True):
        data = {
            "id": self.id,
            "user_id": self.user_id,
            "status": self.status,
            "subtotal": float(self.subtotal),
            "delivery_fee": float(self.delivery_fee),
            "total_amount": float(self.total_amount),
            "delivery_address": self.delivery_address,
            "payment_status": self.payment_status,
            "customer_notes": self.customer_notes,
            "item_count": self.item_count,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "shipped_at": self.shipped_at.isoformat() if self.shipped_at else None,
            "delivered_at": self.delivered_at.isoformat() if self.delivered_at else None,
        }
        if include_items:
            data["items"] = [item.to_dict() for item in self.items]
        return data

class OrderItem(db.Model):
    
    __tablename__ = "order_items"

    id = db.Column(db.Integer, primary_key=True)
    
    # Foreign Keys
    order_id = db.Column(db.Integer, db.ForeignKey("orders.id"), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)
    
    # Quantity 
    quantity = db.Column(db.Integer, nullable=False)
    
    # Price snapshot
    price_at_purchase = db.Column(db.Numeric(10, 2), nullable=False)
    
    # Product name snapshot too 
    product_name_snapshot = db.Column(db.String(200))
    
    # Relationships
    order = db.relationship("Order", back_populates="items")
    product = db.relationship("Product", back_populates="order_items")
   
    @property
    def subtotal(self):
        return float(self.price_at_purchase) * self.quantity

    def to_dict(self):
        return {
            "id": self.id,
            "order_id": self.order_id,
            "product_id": self.product_id,
            "product_name": self.product_name_snapshot or (self.product.name if self.product else "Unknown"),
            "quantity": self.quantity,
            "price_at_purchase": float(self.price_at_purchase),
            "subtotal": self.subtotal,
        }
