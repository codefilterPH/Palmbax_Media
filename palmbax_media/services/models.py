from django.db import models
from django.utils.translation import gettext_lazy as _
from django import forms

# my imports
from banner.validators import *

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

    packages = StreamField([
        ('package_entry', blocks.CharBlock(form_classname="title")),
    ], use_json_field=True)

    description = models.TextField(_('Package Description'),
                                   max_length=200,
                                   null=True,
                                   blank=True,
                                   help_text='Define your package.')

    duration = models.IntegerField(blank=True, null=True,)
    COLOR_CHOICES = [
        ('min', 'min'),
        ('mins', 'mins'),
        ('hour', 'hour'),
        ('hours', 'hours'),
        ('day', 'day'),
        ('days', 'days'),
        ('month', 'month'),
        ('months', 'months'),
        ('year', 'year'),
        ('years', 'years'),

    ]
    unit = models.CharField(_('Time Units'),
                            max_length=7,
                            choices=COLOR_CHOICES,
                            default='hour',
                            blank=True,
                            null=True,
                            )
    price = models.DecimalField(max_digits=10,
                                decimal_places=2,
                                null=True,
                                blank=True,)
    show_price_start = models.BooleanField(_('Show Price Start Tag'),
                                           default=False)
    remarks = models.TextField(_('Package Remarks'),
                               max_length=150,
                               null=True,
                               blank=True,
                               help_text='Enter remarks. Ex: Additional services or information.')

    service_image = models.ForeignKey(
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
        index.SearchField('title'),
        index.FilterField('title'),
        index.RelatedFields('description', [
            index.SearchField('title'),
            index.FilterField('title'),
        ]),
        index.RelatedFields('packages', [
            index.SearchField('title'),
            index.FilterField('title'),
        ])
    ]

    api_fields = [
        APIField('title'),
        APIField('packages'),
        APIField('duration'),
        APIField('unit'),
        APIField('price'),
        APIField('show_price_start'),
        APIField('remarks'),
        APIField('service_image'),
        APIField('service_video'),
        APIField('service_youtube_url'),
        APIField('service_packages'),

    ]

    content_panels = Page.content_panels + [
        FieldPanel('description'),
        FieldRowPanel([
            FieldPanel('duration', classname='Col2'),
            FieldPanel('unit', classname='Col2'),
            FieldPanel('price', classname='Col4'),
            FieldPanel('show_price_start', classname='Col2'),
        ], heading='Package value setup'),
        FieldPanel('remarks'),
        MultiFieldPanel([
            FieldPanel('service_image'),
            FieldRowPanel([
                FieldPanel('service_video', classname='Col8'),
                FieldPanel('service_youtube_url', classname='Col8'),
            ]),
        ], heading='Supporting files'),
        FieldPanel('packages'),
    ]

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Service Page')
        verbose_name_plural = _('Service Pages')

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['live_page_status'] = ServicesPage.objects.live().exists()