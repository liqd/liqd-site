# Website for Liquid Democracy e.V.

Note::

    Work in progress! This isn't meant for general consumption at this stage. Many expected
    things do not work yet!

The website uses the [django-based CMS Wagtail](https://wagtail.io/), and Python 2.7

## How to start

1. clone repository
2. `cd liquidsite`
3. `make install`
4. inside venv run `python manage.py createsuperuser` and create your admin account
9. `make watch`
10. website should be up and running at http://localhost:8006/
11. browse to  http://localhost:8006/admin to login with your admin account
