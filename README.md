# Mappy

Mappy is a Django application to store and show object location on GoogleMaps .

## Requirement
1. [Django](https://https://www.djangoproject.com/) (tested on version 3.1)
2. Python (tested on version 3.8)
3. Google maps API key with Maps JavaScript API enabled [get and API key instruction](https://developers.google.com/maps/documentation/javascript/get-api-key)

## Installation
1. clone this project
```bash
git clone https://github.com/raffaellasuardini/tesi.git
```

2. create a virtual env

```bash
python -m venv env
source env/bin/activate
```

3. install [Django Rest Framework](https://www.django-rest-framework.org/)

```bash
pip install djangorestframework
```
4. install [Django-Environment
](https://django-environ.readthedocs.io/en/latest/)

```bash
pip install django-environ
```

5. create a .env file like this:
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
