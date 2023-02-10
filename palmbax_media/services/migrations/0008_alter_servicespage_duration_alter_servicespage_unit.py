# Generated by Django 4.1.4 on 2023-02-10 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0007_alter_servicespage_packages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicespage',
            name='duration',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='servicespage',
            name='unit',
            field=models.CharField(blank=True, choices=[('min', 'min'), ('mins', 'mins'), ('hour', 'hour'), ('hours', 'hours'), ('day', 'day'), ('days', 'days'), ('month', 'month'), ('months', 'months'), ('year', 'year'), ('years', 'years')], default='hour', max_length=7, null=True, verbose_name='Time Units'),
        ),
    ]