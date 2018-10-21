from flask import render_template, url_for, redirect
from app import app

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]


@app.route('/')
@app.route('/home')
def index():
    return render_template('home.html', posts=posts)


@app.route('/version-<version>/<path:static_file>')
def versioned_static(version, static_file):
    return redirect(static_file)