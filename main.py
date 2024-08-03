from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
from datetime import datetime

app = Flask(__name__)

# Load posts from JSON file
def load_posts():
    try:
        with open('posts.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save posts to JSON file
def save_posts(posts):
    with open('posts.json', 'w') as file:
        json.dump(posts, file, indent=4)

@app.route('/')
def index():
    posts = load_posts()
    return render_template('index.html', posts=posts)

@app.route('/post/<int:post_id>')
def post(post_id):
    posts = load_posts()
    post = next((p for p in posts if p['id'] == post_id), None)
    if post:
        return render_template('post.html', post=post)
    else:
        return 'Post not found', 404

@app.route('/new_post', methods=['GET', 'POST'])
def new_post():
    if request.method == 'POST':
        posts = load_posts()
        new_post = {
            'id': len(posts) + 1,
            'title': request.form['title'],
            'content': request.form['content'],
            'author': request.form['author'],
            'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        posts.append(new_post)
        save_posts(posts)
        return redirect(url_for('index'))
    return render_template('new_post.html')

if __name__ == '__main__':
    app.run(debug=True)
