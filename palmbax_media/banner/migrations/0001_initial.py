# Generated by Django 4.1.4 on 2023-01-04 15:25

import banner.validators
from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0078_referenceindex'),
        ('wagtailimages', '0024_index_image_file_hash'),
    ]

    operations = [
        migrations.CreateModel(
            name='BannerPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
            ],
            options={
                'verbose_name': 'Home Banner',
                'verbose_name_plural': 'Home Banners',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='Banners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('video', models.FileField(blank=True, help_text='Upload Video', max_length=50, null=True, upload_to='banner_videos', validators=[banner.validators.mp4_validate_file_extension], verbose_name='Video Banner')),
                ('url', models.CharField(blank=True, help_text='ex: https://youtube.com/embed/abc123', max_length=200, null=True, verbose_name='Embed Video Link')),
                ('option', models.CharField(choices=[('stream image', 'stream image'), ('stream uploaded video', 'stream uploaded video'), ('stream youtube link', 'stream youtube link')], default='stream image', help_text='select which one to showcase', max_length=200, null=True, verbose_name='Stream Settings')),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='banners', to='banner.bannerpage')),
            ],
            options={
                'verbose_name': 'HOME BANNER',
                'verbose_name_plural': 'HOME BANNERS',
            },
        ),
    ]
