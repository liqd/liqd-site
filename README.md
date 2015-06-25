# Website for Liquid Democracy e.V.

The website uses the [django-based CMS Wagtail](https://wagtail.io/), and Python 2.7

## How to start

1. create virtual env, if you want
2. clone repository
3. run `pip install -r /path/to/liquidsite/requirements.txt`
4. Copy `/path/to/liquidsite/liquidsite/sample.local.py` to `/path/to/liquidsite/liquidsite/local.py`.
5. Set up database connection in local.py (if nothing is changed an sqlite db will be created)
6. run `python manage.py migrate`
7. run `python manage.py createsuperuser` (creates an admin-account, which you can use to login)
8. run `python manage.py load_initial_data` to load some data
9. run `python manage.py runserver` 
10. Website should be up and running at http://localhost:8000/
11. Browse to  http://localhost:8000/admin to login

