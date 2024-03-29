# Generated by Django 4.1.4 on 2023-02-11 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0005_alter_menuitem_link_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='bg_color',
            field=models.CharField(choices=[('#ffffff', 'light'), ('#007bff', 'blue'), ('#37a1fe', 'sky blue'), ('#4caf50', 'green'), ('#7f00ff', 'purple'), ('#3c3c3c', 'dark'), ('#000000', 'black')], default='#ffffff', max_length=7, verbose_name='Background Color'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='font_color',
            field=models.CharField(choices=[('#ffffff', 'light'), ('#007bff', 'blue'), ('#37a1fe', 'sky blue'), ('#4caf50', 'green'), ('#7f00ff', 'purple'), ('#3c3c3c', 'dark'), ('#000000', 'black')], default='#3c3c3c', max_length=7, verbose_name='Font Color'),
        ),
    ]
