# Generated by Django 4.1.4 on 2023-01-14 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banner', '0007_bannerpage_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bannerpage',
            name='banner_title',
            field=models.CharField(help_text="Enter any title of the banner. Ex. Event's page banner.", max_length=50, null=True, verbose_name='Banner Subtitle'),
        ),
    ]
