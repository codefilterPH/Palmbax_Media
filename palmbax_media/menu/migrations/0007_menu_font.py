# Generated by Django 4.1.4 on 2023-02-11 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0006_alter_menu_bg_color_alter_menu_font_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='font',
            field=models.CharField(choices=[("'Sofia Sans', sans-serif", 'Sofia Sans')], default="'Sofia Sans', sans-serif", max_length=50, verbose_name='Font Color'),
        ),
    ]