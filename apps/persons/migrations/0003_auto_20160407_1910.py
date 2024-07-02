# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("persons", "0002_auto_20160401_1835"),
    ]

    operations = [
        migrations.AlterField(
            model_name="personpage",
            name="area",
            field=models.CharField(
                choices=[
                    ("Vorstand", "Vorstand"),
                    ("Projektmanagement", "Projektmanagement"),
                    ("Entwicklung", "Entwicklung"),
                    ("Design", "Design"),
                ],
                max_length=256,
            ),
        ),
    ]
