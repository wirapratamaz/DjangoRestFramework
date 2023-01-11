Build a First API with # DjangoRestFramework

*Steps to creating a REST API*

1. Set up Django
    $ cd folder
    $ virtualenv virtenv
    $ source virtenv/bin/activate
    $ pip install -r requirements.txt
    $ python manage.py makemigrations
    $ python manage.py migrate
    $ python manage.py runserver
2. Create a model in the database that the Django ORM will manage
3. Set up the Django REST Framework
4. Serialize the model from step 2
5. Create the URI endpoints to view the serialized data
