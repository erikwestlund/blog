FROM tiangolo/uwsgi-nginx-flask:python3.7

ENV STATIC_PATH /app/static

RUN pip install --upgrade pip

RUN pip install python-dotenv \
                psycopg2-binary \
                flask-debugtoolbar \
                flask_wtf \
                flask_sqlalchemy \
                flask-redis \
                flask_script \
                Flask-Migrate \
                flask_bcrypt \
                flask-login \
                Flask-Mail \
                redis \
                celery[redis]

COPY ./app /app
