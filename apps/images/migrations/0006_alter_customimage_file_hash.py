# Generated by Django 3.2.13 on 2022-08-22 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("images", "0005_add_img_alt_copyright"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customimage",
            name="file_hash",
            field=models.CharField(
                blank=True, db_index=True, editable=False, max_length=40
            ),
        ),
    ]
