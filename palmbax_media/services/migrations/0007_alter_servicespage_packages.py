# Generated by Django 4.1.4 on 2023-02-10 15:35

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0006_alter_servicespage_packages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicespage',
            name='packages',
            field=wagtail.fields.StreamField([('package_entry', wagtail.blocks.CharBlock(form_classname='title'))], use_json_field=True),
        ),
    ]
