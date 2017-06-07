# -*- coding: utf-8 -*-
from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = u'Load initial Data to Database'

    def handle(self, *args, **options):
        call_command('loaddata', 'initial_data.json', verbosity=0)
