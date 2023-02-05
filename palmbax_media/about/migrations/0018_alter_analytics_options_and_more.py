# Generated by Django 4.1.4 on 2023-02-03 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0017_alter_analyticsettings_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='analytics',
            options={'verbose_name': 'Analytic Entry Page', 'verbose_name_plural': 'Analytic Entry Pages'},
        ),
        migrations.AlterModelOptions(
            name='analyticsettings',
            options={'verbose_name': 'Analytic Setup Page', 'verbose_name_plural': 'Analytics Setup Page'},
        ),
        migrations.AlterField(
            model_name='analytics',
            name='field',
            field=models.CharField(default='No name', help_text='Enter the field name. ex: "Number of clients".', max_length=40, null=True, verbose_name='Field Name'),
        ),
        migrations.AlterField(
            model_name='analytics',
            name='value',
            field=models.PositiveSmallIntegerField(default='0', help_text='Enter the whole number value 1-100+', null=True, verbose_name='Analytic Value'),
        ),
    ]