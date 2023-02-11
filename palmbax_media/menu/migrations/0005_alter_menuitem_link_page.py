# Generated by Django 4.1.4 on 2023-02-11 03:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0078_referenceindex'),
        ('menu', '0004_alter_menuitem_link_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='link_page',
            field=models.ForeignKey(blank=True, help_text='Select only a lived or published page', limit_choices_to={'live': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailcore.page'),
        ),
    ]
