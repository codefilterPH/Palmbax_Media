# Generated by Django 4.1.4 on 2023-02-13 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0018_alter_servicedetailpage_service_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicedetailpage',
            name='feature',
            field=models.BooleanField(default=False, verbose_name='Feature To Home'),
        ),
    ]
