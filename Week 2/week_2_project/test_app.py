import pytest
from book_library_app import book_lib, books

@pytest.fixture
def client():
    book_lib.config['TESTING'] = True
    with book_lib.test_client() as client:
        yield client

def test_home_page(client):
    res = client.get('/')
    assert res.status_code == 200
    assert b"Welcome to the Flask application book library app" in res.data

def test_get_all_books(client):
    res = client.get('/books')
    assert res.status_code == 200
    assert len(res.get_json()['books']) == len(books)

def test_get_specific_book(client):
    res = client.get('/books/1')
    assert res.status_code == 200
    data = res.get_json()
    assert data['book_id'] == 1

def test_create_book(client):
    new_book = {
        "title": "Deep Work",
        "author": "Cal Newport",
        "isbn": "978-0-145-63769-2",
        "year": 2016
    }
    res = client.post('/books', json=new_book)
    assert res.status_code == 201
    assert res.get_json()['new_book']['title'] == "Deep Work"

def test_update_book(client):
    update_data = {"title": "Atomic Habits Updated"}
    res = client.put('/books/1', json=update_data)
    assert res.status_code == 200
    assert res.get_json()['title'] == "Atomic Habits Updated"

def test_delete_book(client):
    res = client.delete('/books/1')
    assert res.status_code == 200
    
    # Deleting again should fail
    res2 = client.delete('/books/1')
    assert res2.status_code == 404
