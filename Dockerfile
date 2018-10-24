FROM tiangolo/uwsgi-nginx-flask:python3.7

ENV STATIC_PATH /app/app/static

RUN pip install --upgrade pip

RUN pip install python-dotenv \
                psycopg2-binary \
                Flask-Versioned \
                flask_wtf \
                flask_sqlalchemy \
                flask_script \
                Flask-Migrate \
                flask_bcrypt \
                flask_login

COPY ./app /app
