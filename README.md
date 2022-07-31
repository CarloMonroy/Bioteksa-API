# Libraries

## Flask

```
Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries. It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions.
```

[Flask](https://flask.palletsprojects.com/en/2.1.x/)

## SQLAlchemy

```
SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.

It provides a full suite of well known enterprise-level persistence patterns, designed for efficient and high-performing database access, adapted into a simple and Pythonic domain language.
```

[SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)

## Docker

```
Docker is an open-source project for automating the deployment of applications as portable, self-sufficient containers that can run on the cloud or on-premises. Docker is also a company that promotes and evolves this technology, working in collaboration with cloud, Linux, and Windows vendors, including Microsoft.

```

## Pytest

```
The pytest framework makes it easy to write small, readable tests, and can scale to support complex functional testing for applications and libraries.
```

## Requirements

### Dockers

### Git

# Run test

If you have pytest installed you can do

```
$ pytest
```

# Installation Instructions

### Clone git

Navigate to your destination directory

```
$ git clone https://github.com/CarloMonroy/Bioteksa-API.git
$ cd Bioteksa-API
```

### Build docker container

```
$ docker build --tag bioteksa-docker .
```

Now you can run the container

```
$ docker run --publish 8000:5000 bioteksa-docker
```

This command runs the container in port 8000/cultivos.
This endpoint takes a get request with params [user_id, page, per_page]
If page or per_page is not defined it will default to 1

It returns a Json with a data object with all the information and a
meta object with pagination information.

Now you can make requests to this api.

example

```
$ curl http://127.0.0.1:8000/cultivos?user_id=2
$ curl http://127.0.0.1:8000/cultivos?user_id=2&per_page=5
```

Response:

```
{
  "data": [
    {
      "nombre": "Tomate",
      "ciclo_cultivo_id": 2,
      "ambiente_cultivo_id": 3,
      "fecha_inicio": "Mon, 28 May 2018 00:00:00 GMT",
      "fecha_final": "Sat, 30 Jun 2018 00:00:00 GMT",
      "clave_cultivo": "yTq5k3WU",
      "creador_id": 2,
      "id": 90,
      "predios_id": 131,
      "tipos_cultivo_id": 3,
      "devices": [
        {
          "nombre": "Botlog 30303433",
          "clave": "Gbav578k",
          "id": 119,
          "tipo_biodispositivos_id": 4,
          "pivot": {
            "cultivos_id": 90,
            "bio_dispositivos_id": 118
          },
          "last_log": [
            {
              "value_datetime": "Thu, 31 May 2018 16:11:34 GMT",
              "pivot": {
                "bio_dispositivos_id": 118,
                "sensores_id": 369
              }
            }
          ],
          "device_type": {
            "id": 4,
            "nombre": "Botlog 30303433",
            "modulos": 0
          }
        },
        {
          "nombre": "Botlog 30303436",
          "clave": "P25Ftr5s",
          "id": 120,
          "tipo_biodispositivos_id": 4,
          "pivot": {
            "cultivos_id": 90,
            "bio_dispositivos_id": 118
          },
          "last_log": [
            {
              "value_datetime": "Thu, 31 May 2018 16:11:35 GMT",
              "pivot": {
                "bio_dispositivos_id": 118,
                "sensores_id": 375
              }
            }
          ],
          "device_type": {
            "id": 4,
            "nombre": "Botlog 30303436",
            "modulos": 0
          }
        }
      ]
    }
  ],
  "meta": {
    "page": 1,
    "pages": 85,
    "total_count": 85,
    "next_page": 2,
    "has_next": true,
    "has_prev": false
  }
}


```

# Instalation no-Docker

If you want to run this without docker we will need to create a virtual environment

inside Bioteksa-API directory

```
$ python3 -m venv venv
```

then we activate the environmante

```
$ source venv/bin/activate
```

On windows (not shure how u do it on windows)

```
$ virtualenv venv
```

We install the required packages from requirements.txt

```
$ pip install -r requirements.txt
```

now we need to export our global variables to be able to connect to the database

```

$ export DB_USERNAME=<username>
$ export DB_PASSWORD=<password>

```

Now we just need to run server.py

```

$ cd src
$ python server.py

```

This time you can acces this api on port 5000
