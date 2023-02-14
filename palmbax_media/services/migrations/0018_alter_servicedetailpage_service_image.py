# Generated by Django 4.1.4 on 2023-02-12 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0024_index_image_file_hash'),
        ('services', '0017_alter_servicedetailpage_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicedetailpage',
            name='service_image',
            field=models.ForeignKey(blank=True, help_text='Best if image size is landscape.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
    ]