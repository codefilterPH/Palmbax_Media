# Generated by Django 4.1.4 on 2023-02-10 15:32

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_alter_servicespage_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicespage',
            name='packages',
            field=wagtail.fields.StreamField([('package_entry', wagtail.blocks.CharBlock(form_classname='title'))], null=True, use_json_field=True),
        ),
    ]