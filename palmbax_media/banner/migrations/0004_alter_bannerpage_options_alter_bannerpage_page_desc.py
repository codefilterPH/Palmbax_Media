# Generated by Django 4.1.4 on 2023-01-14 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banner', '0003_bannerpage_page_desc'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bannerpage',
            options={'verbose_name': 'The Banner', 'verbose_name_plural': 'The Banners'},
        ),
        migrations.AlterField(
            model_name='bannerpage',
            name='page_desc',
            field=models.CharField(help_text='Enter any text. This page will show you all the banners you have.', max_length=500, null=True, verbose_name='Page Description'),
        ),
    ]
