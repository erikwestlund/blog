from flask import render_template, url_for, flash, redirect
from blog import app
from blog.controllers.login_controller import login as login_controller

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


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/login", methods=['GET', 'POST'])
def login():
    return login_controller();

@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route('/version-<version>/<path:static_file>')
def versioned_static(version, static_file):
    return redirect(static_file)