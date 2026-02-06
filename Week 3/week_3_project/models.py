from extensions import db

class BookModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    author = db.Column(db.String(100))
    isbn = db.Column(db.String(50), unique=True)
    year = db.Column(db.Integer)
