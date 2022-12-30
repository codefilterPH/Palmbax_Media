from django.db import models
# Tool
from django.utils.translation import gettext_lazy as _

# Wagtail
from wagtail.admin.panels import (
    FieldPanel, MultiFieldPanel, InlinePanel
)
from wagtail.models import Page, Orderable
from wagtail.search import index
from modelcluster.fields import ParentalKey
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

    api_fields = [
        APIField('banners'),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('banners'),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            InlinePanel('banners', label='banner orderables'),
        ], heading='The Banners')
    ]

    class Meta:
        verbose_name = 'Home Banner'
        verbose_name_plural = 'Home Banners'


class Banners(Orderable):
    stream_option = (
        ('stream image', 'stream image'),
        ('stream uploaded video', 'stream uploaded video'),
        ('stream youtube link', 'stream youtube link'),
    )
    page = ParentalKey(
        'BannerPage',
        on_delete=models.CASCADE,
        related_name='banners'
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
                             help_text='Upload Video')

    url = models.CharField(_('Embed Video Link'),
                           max_length=200,
                           null=True,
                           blank=True,
                           help_text='ex: https://youtube.com/embed/abc123'
                           )

    option = models.CharField(_('Stream Settings'),
                              default='stream image',
                              null=True,
                              max_length= 200,
                              blank=False,
                              help_text='select which one to showcase',
                              choices=stream_option)

    date = models.DateTimeField(auto_now_add=True, null=True)

    panels = [
        FieldPanel('image'),
        FieldPanel('video'),
        FieldPanel('url'),
        FieldPanel('option'),
    ]

    class Meta:
        verbose_name = 'Home Banner'
        verbose_name_plural = 'Home Banners'

