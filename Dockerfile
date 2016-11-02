FROM       ubuntu:14.04
MAINTAINER xyx

RUN apt-get update
RUN apt-get install pip
WORKDIR /data
RUN git clone https://github.com/xieyixue/y.git

WORKDIR /data/y
RUN sh deploy.sh
RUN pip install -r requirements.txt
RUN ./manage.py makemigrations
RUN ./manage.py migrate



EXPOSE 22

CMD    ["/data/y/manage.py", "runserver 0.0.0.0:80"]
