FROM tiangolo/uwsgi-nginx-flask:python3.7

RUN pip install --upgrade pip

RUN pip install Flask-Versioned flask_wtf flask_sqlalchemy flask_bcrypt flask_login python-dotenv

COPY ./app /app
