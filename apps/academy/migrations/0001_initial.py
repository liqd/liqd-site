# Generated by Django 2.2.9 on 2020-06-15 10:35

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcademyPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('title_en', models.CharField(max_length=255, verbose_name='Title')),
                ('title_de', models.CharField(blank=True, max_length=255, verbose_name='Title')),
                ('subtitle_en', models.CharField(default='', max_length=255, verbose_name='Subtitle')),
                ('subtitle_de', models.CharField(blank=True, default='', max_length=255, verbose_name='Subtitle')),
                ('intro_en', wagtail.core.fields.RichTextField(verbose_name='Teasertext')),
                ('intro_de', wagtail.core.fields.RichTextField(blank=True, verbose_name='Teasertext')),
                ('body_en', wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(classname='full title', icon='title')), ('paragraph', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('aligned_image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Image')), ('display', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'left'), ('right', 'right')], help_text='Decide on which side the image should be displayed'))], icon='image')), ('video', wagtail.embeds.blocks.EmbedBlock(icon='media')), ('Raw_HTML', wagtail.core.blocks.StructBlock([('headline', wagtail.core.blocks.CharBlock(length=256, required=False)), ('body', wagtail.core.blocks.RawHTMLBlock())]))], null=True, verbose_name='Body')),
                ('body_de', wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(classname='full title', icon='title')), ('paragraph', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('aligned_image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Image')), ('display', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'left'), ('right', 'right')], help_text='Decide on which side the image should be displayed'))], icon='image')), ('video', wagtail.embeds.blocks.EmbedBlock(icon='media')), ('Raw_HTML', wagtail.core.blocks.StructBlock([('headline', wagtail.core.blocks.CharBlock(length=256, required=False)), ('body', wagtail.core.blocks.RawHTMLBlock())]))], blank=True, null=True, verbose_name='Body')),
                ('author', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.DateField(verbose_name='Post date')),
                ('topics', multiselectfield.db.fields.MultiSelectField(choices=[('LT', 'Liquid Democracy & Theory'), ('DS', 'Digital Civic Society'), ('PA', 'Digital Participation In Action')], max_length=8)),
                ('page_content_type', models.CharField(blank=True, choices=[('VD', 'video'), ('WS', 'workshop'), ('TK', 'talk'), ('LL', 'link list'), ('BP', 'blogpost'), ('WB', 'webinar')], max_length=2)),
            ],
            options={
                'verbose_name': 'Academy Page',
            },
            bases=('wagtailcore.page',),
        ),
    ]