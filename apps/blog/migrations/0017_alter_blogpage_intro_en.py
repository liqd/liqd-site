# Generated by Django 3.2.13 on 2023-02-20 11:10

from django.db import migrations
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_fix_image_block'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='intro_en',
            field=wagtail.fields.RichTextField(blank=True, verbose_name='Teasertext'),
        ),
    ]
