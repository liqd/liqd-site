# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20160222_2322'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectpage',
            name='external_url',
            field=models.CharField(max_length=200, blank=True),
        ),
    ]
