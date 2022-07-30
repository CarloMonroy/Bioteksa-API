# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

WORKDIR /app/src

ENV FLASK_APP=app.py \
    API_USERNAME=biobotTest \
    APP_PASSWORD=shinyWhal322


CMD [ "python3", "app.py"]