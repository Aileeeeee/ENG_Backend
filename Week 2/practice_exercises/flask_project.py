from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/<username>')
def profile_page(username):
    return f"This is {username}'s profile page."

@app.route('/<int:post_id>')
def show_id(post_id):
    return f"{post_id} is my post id."

@app.route('/<path:file_path>')
def secret_path(file_path):
    return f"This is my secret webpage"