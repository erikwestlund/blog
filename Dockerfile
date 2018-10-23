FROM tiangolo/uwsgi-nginx-flask:python3.7

RUN pip install --upgrade pip

RUN pip install python-dotenv \
                Flask-Versioned \
                flask_wtf \
                flask_sqlalchemy \
                Flask-Migrate \
                flask_bcrypt \
                flask_login

COPY ./app /app
