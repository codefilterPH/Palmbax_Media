from django.db import models
from django.utils.translation import gettext_lazy as _
# Wagtail
from wagtail.admin.panels import (
    FieldPanel, MultiFieldPanel, FieldRowPanel
)
from wagtail.models import Page
from wagtail.search import index

# Wagtail Api
from wagtail.api import APIField

# my imports
from .validators import mp4_validate_file_extension


# Create your models here.


class BannerPage(Page):
    parent_page_types = [
        'home.HomePage',
    ]
    template = 'banner/banner_page.html'

    banner_title = models.CharField(_('Banner Subtitle'),
                                    max_length=50,
                                    null=True,
                                    blank=False,
                                    help_text='Enter any title of the banner. Ex. Event\'s page banner.')

    description = models.TextField(_('Page Description'),
                                   max_length=500,
                                   null=True,
                                   blank=False,
                                   help_text='Enter any text to describe your banner.')

    stream_option = (
        ('show image', 'show image'),
        ('stream uploaded video', 'stream uploaded video'),
        ('stream youtube link', 'stream youtube link'),
    )

    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    video = models.FileField(_('Video Banner'),
                             max_length=50,
                             upload_to='banner_videos',
                             null=True,
                             blank=True,
                             validators=[mp4_validate_file_extension],
                             help_text='Upload a video.')

    url = models.CharField(_('Embed Video Link'),
                           max_length=200,
                           null=True,
                           blank=True,
                           help_text='Ex: https://youtube.com/embed/abc123'
                           )

    option = models.CharField(_('Settings'),
                              default='show image',
                              null=True,
                              max_length=200,
                              blank=False,
                              help_text='Select which one to showcase',
                              choices=stream_option)

    type_choices = (
        ('home page', 'home page'),
        ('about page', 'about page'),
        ('contact page', 'contact page'),
        ('blog page', 'blog page'),
        ('event\'s page', 'event\'s page'),
        ('products and services page', 'products and services page'),
        ('talents page', 'talents page'),
    )

    type = models.CharField(_('Type'),
                            default='home page',
                            null=True,
                            max_length=200,
                            blank=False,
                            help_text='Select a banner page type',
                            choices=type_choices)

    date = models.DateTimeField(auto_now_add=True, null=True)

    api_fields = [
        APIField('banner_title'),
        APIField('description'),
        APIField('image'),
        APIField('video'),
        APIField('url'),
        APIField('option'),
        APIField('type'),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('banner_title'),
        index.SearchField('type'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('banner_title'),
        FieldPanel('description'),
        MultiFieldPanel([
            FieldPanel('image'),
            FieldPanel('video'),
            FieldPanel('url'),
        ], heading='Data'),
        FieldRowPanel([
            FieldPanel('type', classname="Col6"),
            FieldPanel('option', classname="Col6"),
        ], heading='Settings'),

    ]

    class Meta:
        verbose_name = 'The Banner'
        verbose_name_plural = 'The Banners'
