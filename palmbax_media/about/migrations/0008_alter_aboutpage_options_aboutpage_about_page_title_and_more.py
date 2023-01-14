# Generated by Django 4.1.4 on 2023-01-14 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0007_alter_aboutpage_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutpage',
            options={'verbose_name': 'About Us Page', 'verbose_name_plural': 'About Us Page'},
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='about_page_title',
            field=models.CharField(default='About Page', help_text='This is the About Page.', max_length=50, null=True, verbose_name='About Page Subtitle'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='page_description',
            field=models.TextField(help_text='Enter any text to describe your banner.', max_length=500, null=True, verbose_name='Page Description'),
        ),
        migrations.AddField(
            model_name='analytics',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='clients',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='testimonials',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]