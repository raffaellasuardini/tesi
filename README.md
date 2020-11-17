# Mappy

Mappy is a Django application to store and show object location on GoogleMaps .

## Requirement
1. [Django](https://https://www.djangoproject.com/) version 3.x
2. Python

## Installation

1. create a virtual env

```bash
python -m venv env
source env/bin/activate
```

2. install [Django Rest Framework](https://www.django-rest-framework.org/) 

```bash
pip install djangorestframework
```

## Usage

To activate server
```bash
python manage.py runserver
```
To apply migration
```bash
python manage.py migrate
```
To collect static
```bash
python manage.py collectstatic
```
To create superuser
```bash
python manage.py createsuperuser
```

## API Usage

connect to this endpoint:
[http://168.119.157.156/api/coord/](http://168.119.157.156/api/coord/)

You can only use POST to insert : 
 * Object label
 * Latitude
 * Longitude


