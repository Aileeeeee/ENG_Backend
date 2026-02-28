# Import all models so Flask-Migrate can discover them when running `flask db migrate`

from ecommerce_app.models.user import User
from ecommerce_app.models.product import Product,Category,Review
from ecommerce_app.models.cart import Cart, CartItem
from ecommerce_app.models.order import Order, OrderItem
from ecommerce_app.models.recommendation import Recommendation



