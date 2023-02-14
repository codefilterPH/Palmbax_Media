from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

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

from booking.models import *


class ServicePage(Page):
    max_count = 1
    parent_page_types = [
        'home.HomePage',
    ]
    subpage_types = [
        'services.ServiceDetailPage',
    ]
    template = 'services/service_page.html'

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Service Page')
        verbose_name_plural = _('Service Pages')

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['live_page_status'] = ServiceDetailPage.objects.live().exists()

        all_pages = ServiceDetailPage.objects.live()
        paginator = Paginator(all_pages, 6)
        page = request.GET.get("page")
        try:
            context['service_data'] = paginator.page(page)
        except PageNotAnInteger:
            context['service_data'] = paginator.page(1)
        except EmptyPage:
            context['service_data'] = paginator.page(paginator.num_pages)

        return context


class ServiceDetailPage(Page):
    parent_page_types = [
        'services.ServicePage',
    ]
    template = 'services/service_detail_page.html'

    packages = StreamField([
        ('package_entry', blocks.CharBlock(form_classname="title")),
    ], use_json_field=True)

    description = models.TextField(_('Package Description'),
                                   max_length=700,
                                   null=True,
                                   blank=True,
                                   help_text='Define your package.')

    duration = models.IntegerField(blank=True, null=True, )
    COLOR_CHOICES = [
        ('min', 'min'),
        ('m\'s', 'mins'),
        ('hr', 'hour'),
        ('hr\'s', 'hours'),
        ('d', 'day'),
        ('d\'s', 'days'),
        ('wk', 'week'),
        ('wk\'s', 'weeks'),
        ('m', 'month'),
        ('mos', 'months'),
        ('yr', 'year'),
        ('yr\'s', 'years'),

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
                                blank=True,
                                )
    show_price_start = models.BooleanField(_('Show Price Start Tag'),
                                           default=False
                                           )
    feature = models.BooleanField(_('Feature To Home'),
                                  default=False,
                                  )
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
        related_name='+',
        help_text='Best if image size is landscape.'
    )
    service_video = models.FileField(_('Service Supporting Video'),
                                     max_length=50,
                                     upload_to='service_videos',
                                     null=True,
                                     blank=True,
                                     validators=[mp4_validate_file_extension],
                                     help_text='Upload a video.')

    service_youtube_url = models.CharField(_('Youtube Video Link'),
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
        APIField('feature'),
        APIField('remarks'),
        APIField('service_image'),
        APIField('service_video'),
        APIField('service_youtube_url'),
        APIField('service_packages'),

    ]

    content_panels = Page.content_panels + [
        FieldPanel('description'),
        FieldRowPanel([
            FieldPanel('duration', classname='Col4'),
            FieldPanel('unit', classname='Col4'),
        ]),
        FieldRowPanel([
            FieldPanel('price', classname='Col4'),
            FieldPanel('show_price_start', classname='Col4'),
            FieldPanel('feature', classname='Col2'),
        ]),
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
        verbose_name = _('All Services Offered')
        verbose_name_plural = _('All Services Offered')

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['live_service_detail_status'] = ServiceDetailPage.objects.live().exists()
        booking_page = BookingPage.objects.live().first()
        context['book_page'] = booking_page.url

        return context
