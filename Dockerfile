FROM tiangolo/uwsgi-nginx-flask:python3.7

RUN pip install --upgrade pip

RUN pip install Flask-Versioned flask_wtf

COPY ./app /app
