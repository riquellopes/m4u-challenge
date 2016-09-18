FROM python:2.7
MAINTAINER Henrique Lopes

ENV PYTHONUNBUFFERED 1

RUN mkdir /web
WORKDIR /web

ADD . /web/

# Installing project dependencies.
RUN pip install -U pip
RUN pip install -r requirements.txt
RUN pip install -r requirements_dev.txt

RUN make makemigrations
RUN make migrate 
