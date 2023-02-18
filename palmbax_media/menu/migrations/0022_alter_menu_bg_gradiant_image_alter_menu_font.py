# Generated by Django 4.1.4 on 2023-02-16 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0021_delete_social_menu_fb_profile_menu_gmail_profile_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='bg_gradiant_image',
            field=models.CharField(choices=[('linear-gradient(135deg, #C33764 10%, #1D2671 100%)', 'Dark Purple Blue'), ('linear-gradient(135deg, #92FFC0 10%, #002661 100%)', 'Aqua Blue'), ('linear-gradient(135deg, #536976 10%, #292E49 100%)', 'Light Dark'), ('linear-gradient(135deg, #FFDB01 10%, #0E197D 100%)', 'Gold Blue'), ('linear-gradient(135deg, #FF9D6C 10%, #BB4E75 100%)', 'BRT Orange & Mod Pink'), ('linear-gradient(135deg, #007adf 10%, #00ecbc 100%)', 'Dark Sky Blue'), ('linear-gradient(135deg, #434343 10%, #000000 100%)', 'Dark Grey')], default='linear-gradient(135deg, #434343 10%, #000000 100%)', max_length=50, verbose_name='Background Gradiant Color'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='font',
            field=models.CharField(choices=[('Sofia Sans, sans-serif', 'Sofia Sans'), ('Open Sans, sans-serif', 'Open Sans'), ('Quicksand, sans-serif', 'Quicksand'), ('none', 'None')], default='Sofia Sans, sans-serif', max_length=50, verbose_name='Font Family'),
        ),
    ]