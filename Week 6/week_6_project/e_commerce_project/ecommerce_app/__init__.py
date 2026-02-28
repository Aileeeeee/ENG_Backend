# Import libraries
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_mail import Mail


# Create instances of extensions
db = SQLAlchemy()
jwt = JWTManager()
migrate = Migrate()
mail = Mail()


# Define function `create_app` 

def create_app(config_name= 'development'):
    app = Flask('__name__')

    # Load configuartion from config file
    from ecommerce_app.config import config
    app.config.from_object(config[config_name])

    # Initialize extensions
    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app,db)
    mail.init_app(app)

    print(app.config.get("SQLALCHEMY_DATABASE_URI"))


    # Register Blueprints

    # Register blueprint for authentication
    from ecommerce_app.routes.auth import auth_bp
    app.register_blueprint(auth_bp,url_prefix ='/api/auth')

    # Register blueprint for products
    from ecommerce_app.routes.products import products_bp
    app.register_blueprint(products_bp,url_prefix ='/api/products')

    # Register blueprint for cart
    from ecommerce_app.routes.cart import cart_bp
    app.register_blueprint(cart_bp,url_prefix ='/api/cart')

    # Register blueprint for orders
    from ecommerce_app.routes.orders import orders_bp
    app.register_blueprint(orders_bp,url_prefix ='/api/orders')

    # Register blueprint for Admin
    from ecommerce_app.routes.admin import admin_bp
    app.register_blueprint(admin_bp,url_prefix ='/api/admin')

    # Register blueprint for recommendation
    from ecommerce_app.routes.recommendations import recommendataions_bp
    app.register_blueprint(recommendataions_bp,url_prefix='/api/recommendatations')

    # Simple route to verify api is runnning
    @app.route('/api/sale')
    def sale_check():
        return {'status':'healthy', 'message': 'Ecommerce API is running'}
    
    return app