import os
import secrets
from flask import Flask, request, jsonify
from flask_jwt_extended import (
    JWTManager, create_access_token,
    jwt_required, get_jwt_identity, get_jwt
)
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from dotenv import load_dotenv

from models import db, User, Post
from schemas import RegisterSchema, LoginSchema, PostSchema

# Load env
load_dotenv()

# Auto-Generate keys
SECRET_KEY = os.getenv("SECRET_KEY") or secrets.token_hex(32)
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY") or secrets.token_hex(32)

app = Flask(__name__)

app.config["SECRET_KEY"] = SECRET_KEY
app.config["JWT_SECRET_KEY"] = JWT_SECRET_KEY
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", "sqlite:///blog.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
jwt = JWTManager(app)

# Define schemas
register_schema = RegisterSchema()
login_schema = LoginSchema()
post_schema = PostSchema()

# Helpers
def admin_required(fn):
    @wraps(fn)
    @jwt_required()
    def wrapper(*args, **kwargs):
        claims = get_jwt()
        if claims.get("role") != "admin":
            return {"error": "Admin access required"}, 403
        return fn(*args, **kwargs)
    return wrapper

# Setup routes 

@app.route("/")
def home():
    return {"message": "Blog API running successfully"}

# Register route
@app.route("/register", methods=["POST"])
def register():
    errors = register_schema.validate(request.get_json())
    if errors:
        return {"errors": errors}, 400

    data = request.get_json()

    if User.query.filter_by(username=data["username"]).first():
        return {"error": "User already exists"}, 409

    user = User(
        username=data["username"],
        password=generate_password_hash(data["password"]),
        role=data.get("role", "user")
    )

    db.session.add(user)
    db.session.commit()

    return {"message": "User registered successfully"}, 201

# Login routes
@app.route("/login", methods=["POST"])
def login():
    errors = login_schema.validate(request.get_json())
    if errors:
        return {"errors": errors}, 400

    data = request.get_json()
    user = User.query.filter_by(username=data["username"]).first()

    if not user or not check_password_hash(user.password, data["password"]):
        return {"error": "Invalid credentials"}, 401

    token = create_access_token(
        identity=user.id,
        additional_claims={"role": user.role}
    )

    return {"access_token": token}

# Create post route
@app.route("/posts", methods=["POST"])
@jwt_required()
def create_post():
    errors = post_schema.validate(request.get_json())
    if errors:
        return {"errors": errors}, 400

    user_id = get_jwt_identity()
    data = request.get_json()

    post = Post(
        title=data["title"],
        content=data["content"],
        user_id=user_id
    )

    db.session.add(post)
    db.session.commit()

    return {"message": "Post created"}, 201

# Get post route
@app.route("/posts", methods=["GET"])
def get_posts():
    posts = Post.query.all()

    return jsonify([
        {
            "id": post.id,
            "title": post.title,
            "content": post.content,
            "created_at": post.created_at
        }
        for post in posts
    ])

# Admin only 
@app.route("/admin/users", methods=["GET"])
@admin_required
def get_users():
    users = User.query.all()

    return jsonify([
        {
            "id": user.id,
            "username": user.username,
            "role": user.role
        }
        for user in users
    ])

#  Run app
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
