# Generated by Django 4.1.4 on 2023-01-14 10:22

import banner.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banner', '0004_alter_bannerpage_options_alter_bannerpage_page_desc'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='banners',
            options={'ordering': ['sort_order']},
        ),
        migrations.AlterField(
            model_name='banners',
            name='option',
            field=models.CharField(choices=[('show image', 'show image'), ('stream uploaded video', 'stream uploaded video'), ('stream youtube link', 'stream youtube link')], default='show image', help_text='Select which one to showcase', max_length=200, null=True, verbose_name='Stream Settings'),
        ),
        migrations.AlterField(
            model_name='banners',
            name='url',
            field=models.CharField(blank=True, help_text='Ex: https://youtube.com/embed/abc123', max_length=200, null=True, verbose_name='Embed Video Link'),
        ),
        migrations.AlterField(
            model_name='banners',
            name='video',
            field=models.FileField(blank=True, help_text='Upload a video.', max_length=50, null=True, upload_to='banner_videos', validators=[banner.validators.mp4_validate_file_extension], verbose_name='Video Banner'),
        ),
    ]