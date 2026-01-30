from flask import Flask, jsonify
import random

app = Flask(__name__)

# Our quotes database (just a Python list for now)
quotes = [
    {
        "id": 1,
        "text": "The only way to do great work is to love what you do.",
        "author": "Steve Jobs"
    },
    {
        "id": 2,
        "text": "Innovation distinguishes between a leader and a follower.",
        "author": "Steve Jobs"
    },
    {
        "id": 3,
        "text": "Life is what happens when you're busy making other plans.",
        "author": "John Lennon"
    },
    {
        "id": 4,
        "text": "The future belongs to those who believe in the beauty of their dreams.",
        "author": "Eleanor Roosevelt"
    },
    {
        "id": 5,
        "text": "It is during our darkest moments that we must focus to see the light.",
        "author": "Aristotle"
    },
    {
        "id": 6,
        "text": "The only impossible journey is the one you never begin.",
        "author": "Tony Robbins"
    },
    {
        "id": 7,
        "text": "In this life we cannot do great things. We can only do small things with great love.",
        "author": "Mother Teresa"
    },
    {
        "id": 8,
        "text": "Success is not final, failure is not fatal: it is the courage to continue that counts.",
        "author": "Winston Churchill"
    }
]

# Route 1: Get a random quote
@app.route('/quote', methods=['GET'])
def get_random_quote():
    random_quote = random.choice(quotes)
    return jsonify(random_quote)

# Route 2: Get all quotes
@app.route('/quotes', methods=['GET'])
def get_all_quotes():
    return jsonify({
        "count": len(quotes),
        "quotes": quotes
    })

# Root route 
@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to the Quotes API!",
        "endpoints": {
            "/quote": "Get a random quote",
            "/quotes": "Get all quotes"
        }
    })

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=5000)