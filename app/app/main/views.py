from flask import Blueprint, render_template, redirect

main = Blueprint('main', __name__, template_folder='templates', static_folder='static')

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


@main.route('/')
def home():
    return render_template('main/home.html', posts=posts)


@main.route('/version-<version>/<path:static_file>')
def versioned_static(version, static_file):
    return redirect(static_file)

