FROM       ubuntu:14.04
MAINTAINER xyx

RUN apt-get update
RUN apt-get -y install python-pip git libmysqlclient-dev python-setuptools python-dev
RUN mkdir /data


RUN pip install Django==1.8.15 MySQL-python==1.2.5 djangorestframework==3.1.0 django-celery==3.1.17 celery==3.1.23

ADD run.sh /run.sh

EXPOSE 80

CMD ["./run.sh"]
