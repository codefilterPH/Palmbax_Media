# Generated by Django 4.1.4 on 2023-02-05 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0011_alter_menu_telephone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='link_icon',
        ),
    ]