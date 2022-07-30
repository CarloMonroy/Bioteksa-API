# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

WORKDIR /app/src

ENV FLASK_APP=app.py \
    DB_USERNAME=biobotTest \
    DB_PASSWORD=shinyWhal322


CMD [ "pytest", "python3", "server.py"]