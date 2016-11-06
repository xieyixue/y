FROM ubuntu:14.04
MAINTAINER xyx_0410@163.com

RUN apt-get update && \
    apt-get -y install python-pip \
    git \
    libmysqlclient-dev \
    python-setuptools \
    python-dev \
    libssl-dev \
    && apt-get clean \
    && apt-get autoclean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN mkdir /app
COPY . /app

ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt

ADD run.sh /run.sh

EXPOSE 80

CMD ["./run.sh"]
