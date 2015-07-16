# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0002_auto_20150710_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personpage',
            name='email',
            field=models.EmailField(max_length=75, blank=True),
            preserve_default=True,
        ),
    ]
