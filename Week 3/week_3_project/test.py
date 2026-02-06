import pytest
from modified_book_library_app import book_lib
from extensions import db
from models import BookModel


@pytest.fixture
def client():
    book_lib.config['TESTING'] = True
    book_lib.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

    with book_lib.test_client() as client:
        with book_lib.app_context():
            db.create_all()
        yield client
        with book_lib.app_context():
            db.drop_all()


def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    data = response.get_json()
    assert 'endpoints' in data


def test_create_book(client):
    payload = {
        "title": "Clean Code",
        "author": "Robert C. Martin",
        "isbn": "9780132350884",
        "year": 2008
    }

    response = client.post('/books', json=payload)
    assert response.status_code == 201

    data = response.get_json()
    assert data['new_book']['title'] == "Clean Code"


def test_get_all_books(client):
    response = client.get('/books')
    assert response.status_code == 200

    data = response.get_json()
    assert 'books' in data
    assert isinstance(data['books'], list)


def test_get_single_book(client):
    book = BookModel(
        title="Refactoring",
        author="Martin Fowler",
        isbn="9780201485677",
        year=1999
    )

    with book_lib.app_context():
        db.session.add(book)
        db.session.commit()
        book_id = book.id

    response = client.get(f'/books/{book_id}')
    assert response.status_code == 200

    data = response.get_json()
    assert data['title'] == "Refactoring"


def test_update_book(client):
    book = BookModel(
        title="Old Title",
        author="Author",
        isbn="9780000000001",
        year=2000
    )

    with book_lib.app_context():
        db.session.add(book)
        db.session.commit()
        book_id = book.id

    response = client.put(
        f'/books/{book_id}',
        json={"title": "New Title"}
    )

    assert response.status_code == 200
    data = response.get_json()
    assert data['title'] == "New Title"


def test_delete_book(client):
    book = BookModel(
        title="Delete Me",
        author="Someone",
        isbn="9780000000002",
        year=2010
    )

    with book_lib.app_context():
        db.session.add(book)
        db.session.commit()
        book_id = book.id

    response = client.delete(f'/books/{book_id}')
    assert response.status_code == 200

    response = client.get(f'/books/{book_id}')
    assert response.status_code == 404
