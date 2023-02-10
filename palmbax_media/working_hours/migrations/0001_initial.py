# Generated by Django 4.1.4 on 2023-02-10 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0078_referenceindex'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkingHoursPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('monday', models.CharField(default='9:00 AM - 5:00 PM', max_length=20)),
                ('tuesday', models.CharField(default='9:00 AM - 5:00 PM', max_length=20)),
                ('wednesday', models.CharField(default='9:00 AM - 5:00 PM', max_length=20)),
                ('thursday', models.CharField(default='9:00 AM - 5:00 PM', max_length=20)),
                ('friday', models.CharField(default='9:00 AM - 5:00 PM', max_length=20)),
                ('saturday', models.CharField(default='Closed', max_length=20)),
                ('sunday', models.CharField(default='Closed', max_length=20)),
            ],
            options={
                'verbose_name': 'Opening Hour',
                'verbose_name_plural': 'Opening Hours',
            },
            bases=('wagtailcore.page',),
        ),
    ]