# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = u'Load initial Data to Database'

    def handle(self, *args, **options):
    	User.objects.create_superuser(username='admin', password='admin', email='admin@test.de')
        call_command('loaddata', 'wagtail_page.json', verbosity=0)
        call_command('loaddata', 'core.json', verbosity=0)
        call_command('loaddata', 'blog.json', verbosity=0)
        call_command('loaddata', 'persons.json', verbosity=0)
        call_command('loaddata', 'projects.json', verbosity=0)
