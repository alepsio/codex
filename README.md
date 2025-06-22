# Digital Product Store

This repository contains a minimal Django project that implements a basic portal for selling digital products. The project includes:

- Product catalog with download links
- User profile page showing orders and support tickets
- Simple responsive templates using Bootstrap

## Requirements

- Python 3
- Django (see `requirements.txt`)

## Running

```
python manage.py migrate  # create database tables
python manage.py createsuperuser  # create admin user
python manage.py runserver
```
Migrations are included, so running `python manage.py migrate` will set up the database.

Visit `http://localhost:8000/` to see the store.
