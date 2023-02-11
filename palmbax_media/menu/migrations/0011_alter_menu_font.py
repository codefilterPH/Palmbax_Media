# Generated by Django 4.1.4 on 2023-02-11 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0010_alter_menu_font'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='font',
            field=models.CharField(choices=[("'Sofia Sans', sans-serif", 'Sofia Sans'), ("'Open Sans', sans-serif", 'Open Sans'), ("'Quicksand', sans-serif", 'Quicksand'), ('none', 'None')], default="'Sofia Sans', sans-serif", max_length=50, verbose_name='Font Color'),
        ),
    ]
