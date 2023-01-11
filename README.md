Build a First API with # DjangoRestFramework

*Steps to creating a REST API*

1. Set up Django
    <br>
    $ cd folder
    <br>
    $ virtualenv virtenv
    <br>
    $ source virtenv/bin/activate
    <br>
    $ pip install -r requirements.txt
    <br>
    $ python manage.py makemigrations
    <br>
    $ python manage.py migrate
    <br>
    $ python manage.py runserver
    <br>
2. Create a model in the database that the Django ORM will manage
3. Set up the Django REST Framework
4. Serialize the model from step 2
5. Create the URI endpoints to view the serialized data

*Technology Stack*
Tools used during the development of this API are;
1. Django - a python web framework
2. Django REST Framework - a flexible toolkit to build web APIs
3. SQLite - this is a database server
