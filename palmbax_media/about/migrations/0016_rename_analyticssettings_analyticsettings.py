# Generated by Django 4.1.4 on 2023-02-03 08:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0024_index_image_file_hash'),
        ('about', '0015_analyticssettings'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AnalyticsSettings',
            new_name='AnalyticSettings',
        ),
    ]
