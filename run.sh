#!/bin/bash

cp /data/local_settings.py /app/y/y/local_settings.py
cd /app/y
useradd celery
./manage.py migrate
su celery -c './manage.py celery worker --loglevel=info -c 1' &
./manage.py runserver 0.0.0.0:80
