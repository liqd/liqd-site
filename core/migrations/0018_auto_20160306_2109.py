# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_auto_20160306_2101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='textpage',
            name='body_de',
        ),
        migrations.RemoveField(
            model_name='textpage',
            name='body_en',
        ),
    ]
