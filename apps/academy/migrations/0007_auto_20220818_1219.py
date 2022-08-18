# Generated by Django 3.2.13 on 2022-08-18 10:19

from django.db import migrations
import wagtail.blocks
import wagtail.embeds.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0006_change_blogpost_to_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academychallengepage',
            name='body_de',
            field=wagtail.fields.StreamField([('challenge_tasks', wagtail.blocks.StructBlock([('challenge_step_title', wagtail.blocks.CharBlock()), ('challenge_step_text', wagtail.blocks.RichTextBlock(required=False)), ('links', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('challenge_step_academy_links', wagtail.blocks.PageChooserBlock(page_type=['academy.AcademyPage'], required=False)), ('challenge_step_external_links', wagtail.blocks.PageChooserBlock(page_type=['academy.AcademyExternalLink'], required=False))])))]))], blank=True, null=True, use_json_field=True, verbose_name='Challenge step'),
        ),
        migrations.AlterField(
            model_name='academychallengepage',
            name='body_en',
            field=wagtail.fields.StreamField([('challenge_tasks', wagtail.blocks.StructBlock([('challenge_step_title', wagtail.blocks.CharBlock()), ('challenge_step_text', wagtail.blocks.RichTextBlock(required=False)), ('links', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('challenge_step_academy_links', wagtail.blocks.PageChooserBlock(page_type=['academy.AcademyPage'], required=False)), ('challenge_step_external_links', wagtail.blocks.PageChooserBlock(page_type=['academy.AcademyExternalLink'], required=False))])))]))], null=True, use_json_field=True, verbose_name='Challenge step'),
        ),
        migrations.AlterField(
            model_name='academypage',
            name='body_de',
            field=wagtail.fields.StreamField([('heading', wagtail.blocks.CharBlock(form_classname='full title', icon='title')), ('paragraph', wagtail.blocks.RichTextBlock(icon='pilcrow')), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('aligned_image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Image')), ('display', wagtail.blocks.ChoiceBlock(choices=[('center', 'center'), ('left', 'left'), ('right', 'right')], help_text='Decide on which side the image should be displayed'))], icon='image')), ('video', wagtail.embeds.blocks.EmbedBlock(icon='media')), ('Raw_HTML', wagtail.blocks.StructBlock([('headline', wagtail.blocks.CharBlock(length=256, required=False)), ('body', wagtail.blocks.RawHTMLBlock())]))], blank=True, null=True, use_json_field=True, verbose_name='Body'),
        ),
        migrations.AlterField(
            model_name='academypage',
            name='body_en',
            field=wagtail.fields.StreamField([('heading', wagtail.blocks.CharBlock(form_classname='full title', icon='title')), ('paragraph', wagtail.blocks.RichTextBlock(icon='pilcrow')), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('aligned_image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Image')), ('display', wagtail.blocks.ChoiceBlock(choices=[('center', 'center'), ('left', 'left'), ('right', 'right')], help_text='Decide on which side the image should be displayed'))], icon='image')), ('video', wagtail.embeds.blocks.EmbedBlock(icon='media')), ('Raw_HTML', wagtail.blocks.StructBlock([('headline', wagtail.blocks.CharBlock(length=256, required=False)), ('body', wagtail.blocks.RawHTMLBlock())]))], null=True, use_json_field=True, verbose_name='Body'),
        ),
    ]