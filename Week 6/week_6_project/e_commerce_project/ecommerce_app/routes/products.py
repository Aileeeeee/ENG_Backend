# app/routes/products.py

from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from ecommerce_app import db
from ecommerce_app.models.product import Product, Category, Review
from ecommerce_app.schemas.product_schema import ProductSchema, CategorySchema, ReviewSchema
from app.utils.helpers import success_response, error_response, admin_required
from marshmallow import ValidationError

products_bp = Blueprint("products", __name__)

product_schema = ProductSchema()
category_schema = CategorySchema()
review_schema = ReviewSchema()


# GET /api/products  →  list all products (+ ?search=)
@products_bp.route("/", methods=["GET"])
def get_products():
    search = request.args.get("search", "").strip()

    query = Product.query.filter(Product.is_active == True)

    if search:
        search_term = f"%{search}%"
        query = query.filter(
            db.or_(
                Product.name.ilike(search_term),
                Product.description.ilike(search_term)
            )
        )

    products = query.order_by(Product.name.asc()).all()
    return success_response("Products retrieved", {"products": [p.to_dict() for p in products]})


# GET /api/products/<id>  →  get one product
@products_bp.route("/<int:product_id>", methods=["GET"])
def get_product(product_id):
    product = Product.query.get_or_404(product_id, description="Product not found")

    if not product.is_active:
        return error_response("Product not found", 404)

    return success_response("Product retrieved", {"product": product.to_dict()})


# POST /api/products  →  create product (admin only)
@products_bp.route("/", methods=["POST"])
@jwt_required()
@admin_required
def create_product():
    data = request.get_json()

    if not data:
        return error_response("Request body must be JSON", 400)

    try:
        validated_data = product_schema.load(data)
    except ValidationError as e:
        return error_response("Validation failed", 400, errors=e.messages)

    product = Product(**validated_data)
    db.session.add(product)
    db.session.commit()

    return success_response("Product created", {"product": product.to_dict()}, 201)


# PUT /api/products/<id>  →  update product (admin only)
@products_bp.route("/<int:product_id>", methods=["PUT"])
@jwt_required()
@admin_required
def update_product(product_id):
    product = Product.query.get_or_404(product_id, description="Product not found")

    data = request.get_json()

    if not data:
        return error_response("Request body must be JSON", 400)

    try:
        validated_data = product_schema.load(data, partial=True)
    except ValidationError as e:
        return error_response("Validation failed", 400, errors=e.messages)

    for key, value in validated_data.items():
        setattr(product, key, value)

    db.session.commit()
    return success_response("Product updated", {"product": product.to_dict()})


# DELETE /api/products/<id>  →  soft delete (admin only)
@products_bp.route("/<int:product_id>", methods=["DELETE"])
@jwt_required()
@admin_required
def delete_product(product_id):
    product = Product.query.get_or_404(product_id, description="Product not found")

    product.is_active = False
    db.session.commit()

    return success_response("Product deleted")


# GET /api/products/categories  →  list all categories
@products_bp.route("/categories", methods=["GET"])
def get_categories():
    categories = Category.query.all()
    return success_response("Categories retrieved", {"categories": [c.to_dict() for c in categories]})


# POST /api/products/<id>/reviews  →  add a review (logged in users)
@products_bp.route("/<int:product_id>/reviews", methods=["POST"])
@jwt_required()
def add_review(product_id):
    Product.query.get_or_404(product_id, description="Product not found")
    current_user_id = get_jwt_identity()

    existing_review = Review.query.filter_by(
        product_id=product_id,
        user_id=current_user_id
    ).first()

    if existing_review:
        return error_response("You have already reviewed this product", 409)

    data = request.get_json()

    if not data:
        return error_response("Request body must be JSON", 400)

    try:
        validated_data = review_schema.load(data)
    except ValidationError as e:
        return error_response("Validation failed", 400, errors=e.messages)

    review = Review(
        product_id=product_id,
        user_id=current_user_id,
        **validated_data
    )
    db.session.add(review)
    db.session.commit()

    return success_response("Review added", {"review": review.to_dict()}, 201)

