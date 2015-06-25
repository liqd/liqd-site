# Website for Liquid Democracy e.V.

The website uses the [django-based CMS Wagtail](https://wagtail.io/), and Python 2.7

## How to start

1. create virtual env, if you want
2. clone repository
3. run `pip install -r /path/to/liquidsite/requirements.txt`
4. Copy `/path/to/liquidsite/liquidsite/sample.local.py` to `/path/to/liquidsite/liquidsite/local.py`.
5. Set up database connection (if nothing is changed an sqlite db will be created) in local.py
6. run `python manage.py mirate`
7. run `python manage.py createsuperuser` (creates an admin-account, which you can use to login)
8. run `python manage.py runserver` 
9. Website should be up and running at http://localhost:8000/
10. Browse to  http://localhost:8000/admin to login

