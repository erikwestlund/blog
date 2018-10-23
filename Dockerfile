FROM tiangolo/uwsgi-nginx-flask:python3.7

RUN pip install --upgrade pip

RUN pip install python-dotenv \
                psycopg2 \
                Flask-Versioned \
                flask_wtf \
                flask_sqlalchemy \
                flask_script \
                Flask-Migrate \
                flask_bcrypt \
                flask_login

COPY ./app /app
