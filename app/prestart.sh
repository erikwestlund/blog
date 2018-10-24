#! /usr/bin/env bash

# Let the DB start
sleep 10;

python manage.py db init
python manage.py db migrate
python manage.py db upgrade

echo "test"