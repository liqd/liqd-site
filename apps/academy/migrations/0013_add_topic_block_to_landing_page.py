# Generated by Django 3.2.13 on 2022-08-25 09:26

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0012_fix_max_length'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academylandingpage',
            name='body_de',
            field=wagtail.fields.StreamField([('single_teaser', wagtail.blocks.StructBlock([('category', wagtail.blocks.CharBlock(max_length=32, required=False)), ('headline', wagtail.blocks.CharBlock(max_length=74, required=True)), ('body_text', wagtail.blocks.TextBlock(max_length=164, required=True)), ('link', wagtail.blocks.PageChooserBlock(help_text='Please only add either an internal or external link', required=False)), ('external_link', wagtail.blocks.URLBlock(help_text='The external link overwrites the link to a local page.', label='External Link', required=False)), ('link_text', wagtail.blocks.CharBlock(max_length=24, required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(required=True))])), ('call_to_action_teaser', wagtail.blocks.StructBlock([('columns', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('headline', wagtail.blocks.CharBlock(max_length=28, required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Please add image with transparent background', required=True)), ('body_text', wagtail.blocks.TextBlock(max_length=120, required=True)), ('cta_link', wagtail.blocks.StructBlock([('internal_link', wagtail.blocks.PageChooserBlock(help_text='The external link overwrites the link to a local page. Please only add 1 link.', required=False)), ('external_link', wagtail.blocks.URLBlock(required=False))])), ('link_text', wagtail.blocks.CharBlock(label='Link Text', max_length=28, required=False)), ('anchor_link', wagtail.blocks.CharBlock(help_text='Anchor link should be all one word.', label='Anchor Link', max_length=28, required=False))], label='List and Image'), max_num=2))])), ('topic_block_list', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(max_length=74, required=True)), ('topics', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('topic_category', wagtail.blocks.ChoiceBlock(choices=[('LT', 'Liquid Democracy: Theory & Vision'), ('DS', 'Digital Civic Society'), ('PA', 'Digital Participation In Action')], help_text='Select a topic')), ('topic_text', wagtail.blocks.CharBlock(max_length=110, required=True)), ('topic_link_text', wagtail.blocks.CharBlock(max_length=40, required=True))]), max_num=3, min_num=3)), ('topic_url', wagtail.blocks.PageChooserBlock(page_type=['academy.AcademyIndexPage'], required=True))]))], blank=True, null=True, use_json_field=True, verbose_name='Body'),
        ),
        migrations.AlterField(
            model_name='academylandingpage',
            name='body_en',
            field=wagtail.fields.StreamField([('single_teaser', wagtail.blocks.StructBlock([('category', wagtail.blocks.CharBlock(max_length=32, required=False)), ('headline', wagtail.blocks.CharBlock(max_length=74, required=True)), ('body_text', wagtail.blocks.TextBlock(max_length=164, required=True)), ('link', wagtail.blocks.PageChooserBlock(help_text='Please only add either an internal or external link', required=False)), ('external_link', wagtail.blocks.URLBlock(help_text='The external link overwrites the link to a local page.', label='External Link', required=False)), ('link_text', wagtail.blocks.CharBlock(max_length=24, required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(required=True))])), ('call_to_action_teaser', wagtail.blocks.StructBlock([('columns', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('headline', wagtail.blocks.CharBlock(max_length=28, required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Please add image with transparent background', required=True)), ('body_text', wagtail.blocks.TextBlock(max_length=120, required=True)), ('cta_link', wagtail.blocks.StructBlock([('internal_link', wagtail.blocks.PageChooserBlock(help_text='The external link overwrites the link to a local page. Please only add 1 link.', required=False)), ('external_link', wagtail.blocks.URLBlock(required=False))])), ('link_text', wagtail.blocks.CharBlock(label='Link Text', max_length=28, required=False)), ('anchor_link', wagtail.blocks.CharBlock(help_text='Anchor link should be all one word.', label='Anchor Link', max_length=28, required=False))], label='List and Image'), max_num=2))])), ('topic_block_list', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(max_length=74, required=True)), ('topics', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('topic_category', wagtail.blocks.ChoiceBlock(choices=[('LT', 'Liquid Democracy: Theory & Vision'), ('DS', 'Digital Civic Society'), ('PA', 'Digital Participation In Action')], help_text='Select a topic')), ('topic_text', wagtail.blocks.CharBlock(max_length=110, required=True)), ('topic_link_text', wagtail.blocks.CharBlock(max_length=40, required=True))]), max_num=3, min_num=3)), ('topic_url', wagtail.blocks.PageChooserBlock(page_type=['academy.AcademyIndexPage'], required=True))]))], null=True, use_json_field=True, verbose_name='Body'),
        ),
    ]
