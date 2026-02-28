# Import libraries
from ecommerce_app import db
from datetime import datetime

class Recommendation(db.Model):

    __tablename__ = "recommendations"

    id = db.Column(db.Integer, primary_key=True)

    # The product the customer is currently viewing
    source_product_id = db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)

    # The product we are suggesting
    recommended_product_id = db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # --- Relationships ---
    source_product = db.relationship("Product", foreign_keys=[source_product_id])
    recommended_product = db.relationship("Product", foreign_keys=[recommended_product_id])

    def to_dict(self):
        return {
            "id": self.id,
            "source_product_id": self.source_product_id,
            "recommended_product_id": self.recommended_product_id,
            "recommended_product": self.recommended_product.to_dict() if self.recommended_product else None,
            "created_at": self.created_at.isoformat() if self.created_at else None,
        }

    def __repr__(self):
        return f"<Recommendation Product#{self.source_product_id} → Product#{self.recommended_product_id}>"

