# Generated by Django 3.2.13 on 2023-01-09 14:45

from django.db import migrations
import wagtail.blocks
import wagtail.documents.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_add_new_video_block'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='body_de',
            field=wagtail.fields.StreamField([('heading', wagtail.blocks.CharBlock(form_classname='full title', icon='title')), ('paragraph', wagtail.blocks.RichTextBlock(icon='pilcrow')), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('aligned_image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Image')), ('display', wagtail.blocks.ChoiceBlock(choices=[('center', 'center'), ('left', 'left'), ('right', 'right')], help_text='Decide on which side the image should be displayed'))], icon='image')), ('Raw_HTML', wagtail.blocks.StructBlock([('headline', wagtail.blocks.CharBlock(max_length=256, required=False)), ('body', wagtail.blocks.RawHTMLBlock())])), ('video_block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(max_length=130, required=False)), ('description', wagtail.blocks.CharBlock(help_text='Please insert a short description of the video (character limit 500).', max_length=500, required=False)), ('media', wagtail.documents.blocks.DocumentChooserBlock(help_text='Please upload or choose a media file with any of the following extensions: MP4, WebM, MP3, WAV')), ('media_type', wagtail.blocks.ChoiceBlock(choices=[('audio', 'Audio file'), ('video', 'Video file')])), ('transcript', wagtail.blocks.RichTextBlock(features=['bold', 'italic', 'ol', 'ul', 'link', 'document-link'], help_text="You can add the video's transcript here (unlimited characters).", required=False))]))], blank=True, null=True, use_json_field=True, verbose_name='Body'),
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='body_en',
            field=wagtail.fields.StreamField([('heading', wagtail.blocks.CharBlock(form_classname='full title', icon='title')), ('paragraph', wagtail.blocks.RichTextBlock(icon='pilcrow')), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('aligned_image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Image')), ('display', wagtail.blocks.ChoiceBlock(choices=[('center', 'center'), ('left', 'left'), ('right', 'right')], help_text='Decide on which side the image should be displayed'))], icon='image')), ('Raw_HTML', wagtail.blocks.StructBlock([('headline', wagtail.blocks.CharBlock(max_length=256, required=False)), ('body', wagtail.blocks.RawHTMLBlock())])), ('video_block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(max_length=130, required=False)), ('description', wagtail.blocks.CharBlock(help_text='Please insert a short description of the video (character limit 500).', max_length=500, required=False)), ('media', wagtail.documents.blocks.DocumentChooserBlock(help_text='Please upload or choose a media file with any of the following extensions: MP4, WebM, MP3, WAV')), ('media_type', wagtail.blocks.ChoiceBlock(choices=[('audio', 'Audio file'), ('video', 'Video file')])), ('transcript', wagtail.blocks.RichTextBlock(features=['bold', 'italic', 'ol', 'ul', 'link', 'document-link'], help_text="You can add the video's transcript here (unlimited characters).", required=False))]))], blank=True, null=True, use_json_field=True, verbose_name='Body'),
        ),
    ]
