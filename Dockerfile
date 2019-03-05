FROM tiangolo/uwsgi-nginx-flask:python3.7

#RUN pip install --upgrade pip
COPY ./app /app

RUN pip install -r /app/requirements.txt
