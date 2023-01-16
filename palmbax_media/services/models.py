from django.db import models
from django.utils.translation import gettext_lazy as _
from django import forms

# my imports
from banner.validators import mp4_validate_file_extension

# Wagtail
from wagtail.admin.panels import (
    FieldPanel, MultiFieldPanel, InlinePanel, FieldRowPanel
)

from wagtail.models import Page, Orderable
from wagtail.search import index
from modelcluster.fields import ParentalKey
from wagtail import blocks
from wagtail.fields import StreamField

# wagtail API
from wagtail.api import APIField


class ServicesPage(Page):
    parent_page_types = [
        'home.HomePage',
    ]
    template = 'services/services_page.html'
    date = models.DateTimeField(auto_now_add=True, null=True)
    services_page_title = models.CharField(_('Services Page Subtitle'),
                                           max_length=50,
                                           null=True,
                                           blank=False,
                                           help_text='This is the Services Page. Add new service that you offered.')

    page_description = models.TextField(_('Page Description'),
                                        max_length=500,
                                        null=True,
                                        blank=False,
                                        help_text='Enter any text to describe your service.')

    service_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    service_background_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    service_video = models.FileField(_('Service Supporting Video'),
                                     max_length=50,
                                     upload_to='banner_videos',
                                     null=True,
                                     blank=True,
                                     validators=[mp4_validate_file_extension],
                                     help_text='Upload a video.')

    service_youtube_url = models.CharField(_('Embed Youtube Video Link'),
                                           max_length=200,
                                           null=True,
                                           blank=True,
                                           help_text='Ex: https://youtube.com/embed/abc123'
                                           )

    search_fields = Page.search_fields + [
        index.SearchField('services_page_title'),
    ]

    api_fields = [
        APIField('services_page_title'),
        APIField('page_description'),
        APIField('date'),
        APIField('service_image'),
        APIField('service_video'),
        APIField('service_youtube_url'),
        APIField('service_packages'),

    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('services_page_title'),
            FieldPanel('page_description'),
        ], heading='Page Information'),
        MultiFieldPanel([
            FieldPanel('service_image'),
            FieldPanel('service_background_image'),
            FieldRowPanel([
                FieldPanel('service_video', classname='Col8'),
                FieldPanel('service_youtube_url', classname='Col8'),
            ]),
        ], heading='Supporting files'),
        MultiFieldPanel([
            InlinePanel('service_packages', label='Packages Offered'),
        ], heading='Packages Offered'),
    ]

    class Meta:
        verbose_name = _('Service Page')
        verbose_name_plural = _('Services Page')


class ServicesPackage(Orderable):
    page = ParentalKey(
        'ServicesPage',
        on_delete=models.CASCADE,
        related_name='service_packages',
    )

    package_title = models.CharField(_('Package Title'),
                                     max_length=200,
                                     null=True,
                                     blank=False,
                                     help_text='You are adding a new package. Ex: Wedding Package, Corporate Party '
                                               'and etc.')

    description = models.TextField(_('Package Description'),
                                   max_length=200,
                                   null=True,
                                   blank=False,
                                   help_text='You are adding a new package. Ex: Wedding Packages and Corporate Party '
                                             'Packages to support this service.')

    package_content = StreamField([
        ('package_entry', blocks.CharBlock(form_classname="title")),
    ], use_json_field=True)

    panels = [
        FieldPanel('package_title'),
        FieldPanel('description'),
        FieldPanel('package_content'),
    ]

    class Meta:
        verbose_name = 'Package Information'
        verbose_name_plural = 'Packages Information'
