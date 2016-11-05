#!/bin/bash

cd y && git pull || git clone https://github.com/xieyixue/y.git
cd /data/y
cp /data/local_settings.py y/local_settings.py
./manage.py makemigrations
./manage.py migrate
./manage.py runserver 0.0.0.0:80
