# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("persons", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="personpage",
            name="email",
            field=models.EmailField(max_length=254, blank=True),
        ),
    ]
