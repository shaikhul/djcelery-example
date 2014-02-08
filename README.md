djcelery-example
================

Django Celery RabbitMQ Simple Example

Prerequisites

1. RabbitMQ ( google RabbitMQ installation)

2. SQLite3 (google SQLite3 about how to set it up with Django)

3. Django

4. django-celery



I have added a regular task and a periodic task in cleanup_manager app. 


Commands:

1. `pip install -r djcelery_example/requirements.txt`

2. create a sqlite db and update the database name in settings.py

3. start rabbitMQ server

4. sync database command: `python manage.py syncdb` 

5. run celery worker: `python manage.py celery worker --loglevel=debug`

6. run celer beat: `python managely.py celery beat --loglevel=debug`

Enjoy Celery ...
