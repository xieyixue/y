#!/bin/bash

mkdir /data
cd /data
git clone https://github.com/xieyixue/y.git || git pull
cd /data/y
cp /data/local_settings.py y/local_settings.py
./manage.py makemigrations
./manage.py migrate
./manage.py runserver 0.0.0.0:80
