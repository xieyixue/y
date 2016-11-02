FROM       ubuntu:14.04
MAINTAINER xyx

RUN apt-get update
RUN apt-get install python-pip git
RUN mkdir /data

WORKDIR /data
RUN git clone https://github.com/xieyixue/y.git

WORKDIR /data/y
RUN sh deploy.sh
RUN pip install -r requirements.txt

ADD run.sh

EXPOSE 80

CMD    ["run.sh"]
