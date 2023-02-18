# Generated by Django 4.1.4 on 2023-02-18 23:39

from django.db import migrations
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0004_alter_peoplepage_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peoplepage',
            name='details',
            field=wagtail.fields.RichTextField(blank=True, default='None', help_text="Please person's best description.", null=True, verbose_name='Details'),
        ),
    ]
