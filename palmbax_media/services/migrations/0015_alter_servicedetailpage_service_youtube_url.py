# Generated by Django 4.1.4 on 2023-02-12 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0014_alter_servicedetailpage_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicedetailpage',
            name='service_youtube_url',
            field=models.CharField(blank=True, help_text='Ex: https://youtube.com/embed/abc123', max_length=200, null=True, verbose_name='Youtube Video Link'),
        ),
    ]
