# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_auto_20160224_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectpage',
            name='external_url',
            field=models.URLField(blank=True),
        ),
    ]
