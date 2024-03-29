# Generated by Django 4.1.4 on 2023-02-11 05:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0078_referenceindex'),
        ('wagtailimages', '0024_index_image_file_hash'),
        ('services', '0008_alter_servicespage_duration_alter_servicespage_unit'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServicePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
            ],
            options={
                'verbose_name': 'Service Page',
                'verbose_name_plural': 'Service Pages',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.RenameModel(
            old_name='ServicesPage',
            new_name='ServiceDetailPage',
        ),
        migrations.AlterModelOptions(
            name='servicedetailpage',
            options={'verbose_name': 'Service Detail Page', 'verbose_name_plural': 'Service Detail Page'},
        ),
    ]
