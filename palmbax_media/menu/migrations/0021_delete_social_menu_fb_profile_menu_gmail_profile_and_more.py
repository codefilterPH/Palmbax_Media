# Generated by Django 4.1.4 on 2023-02-16 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0020_social'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Social',
        ),
        migrations.AddField(
            model_name='menu',
            name='fb_profile',
            field=models.CharField(blank=True, help_text='Ex. https://www.facebook.com/codefilterph', max_length=500, verbose_name='Facebook Profile'),
        ),
        migrations.AddField(
            model_name='menu',
            name='gmail_profile',
            field=models.CharField(blank=True, max_length=500, verbose_name='Gmail Profile'),
        ),
        migrations.AddField(
            model_name='menu',
            name='instagram_profile',
            field=models.CharField(blank=True, max_length=500, verbose_name='Instagram Profile'),
        ),
        migrations.AddField(
            model_name='menu',
            name='linked_profile',
            field=models.CharField(blank=True, max_length=500, verbose_name='Linkedin Profile'),
        ),
        migrations.AddField(
            model_name='menu',
            name='twitter_profile',
            field=models.CharField(blank=True, max_length=500, verbose_name='Twitter Profile'),
        ),
    ]