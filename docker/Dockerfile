FROM python:3

RUN apt-get -y update

RUN apt-get -y upgrade

RUN apt-get install -y vim

RUN apt-get install rabbitmq-server -y

RUN pip3 install virtualenv

RUN mkdir /nameko_teste

RUN virtualenv /nameko_teste
#--no-site-packages to isolate environment from the main site packages directory

#RUN ./activate

RUN /nameko_teste/bin/pip3 install nameko

WORKDIR /nameko_teste/

RUN git clone https://github.com/nameko/nameko.git setup

WORKDIR /nameko_teste/setup

RUN python setup.py install

WORKDIR /nameko_teste/

COPY ./ .