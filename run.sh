#!/bin/bash

cp /data/local_settings.py /app/y/local_settings.py
cd /app/y
./manage.py migrate
./manage.py runserver 0.0.0.0:80
