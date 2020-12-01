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
3. install [Django-Environment
](https://django-environ.readthedocs.io/en/latest/)

```bash
pip install django-environ
```
Note: no need to add it to INSTALLED_APPS inside django's settings

4. create a .env file like this:
```bash
DEBUG=ON
SECRET_KEY=your_secret_key
GOOGLE_MAP_KEY=your_api_key
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

You can only use POST to insert new coords with a request to the endpoint:
```bash
http://YOUR_DOMAIN/api/coord/
```

JSON Request format:
```bash
{
  object_label: 'label for the point',
  lat: 'latitude',
  lng: 'longitude'
}
```
