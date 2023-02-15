# Generated by Django 4.1.4 on 2023-02-15 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0019_alter_menu_font'),
    ]

    operations = [
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='Social Media Accounts', max_length=50)),
                ('fb_profile', models.CharField(blank=True, help_text='Ex. https://www.facebook.com/codefilterph', max_length=500, verbose_name='Facebook Profile')),
                ('twitter_profile', models.CharField(blank=True, max_length=500, verbose_name='Twitter Profile')),
                ('gmail_profile', models.CharField(blank=True, max_length=500, verbose_name='Gmail Profile')),
                ('instagram_profile', models.CharField(blank=True, max_length=500, verbose_name='Instagram Profile')),
                ('linked_profile', models.CharField(blank=True, max_length=500, verbose_name='Linkedin Profile')),
            ],
            options={
                'verbose_name': 'Social Media Accounts',
            },
        ),
    ]