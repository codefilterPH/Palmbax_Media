from django.db import models
# Tools
# Wagtail
from wagtail.admin.panels import (
    FieldPanel, MultiFieldPanel
)
from wagtail.models import Page
from wagtail.search import index

# wagtail API
from wagtail.api import APIField


# Create your models here.


class WorkingHoursPage(Page):
    max_count = 1
    parent_page_types = [
        'home.HomePage',
    ]
    template = 'working_hours/working_hour_page.html'

    monday = models.CharField(max_length=20, default='9:00 AM - 5:00 PM')
    tuesday = models.CharField(max_length=20, default='9:00 AM - 5:00 PM')
    wednesday = models.CharField(max_length=20, default='9:00 AM - 5:00 PM')
    thursday = models.CharField(max_length=20, default='9:00 AM - 5:00 PM')
    friday = models.CharField(max_length=20, default='9:00 AM - 5:00 PM')
    saturday = models.CharField(max_length=20, default='Closed')
    sunday = models.CharField(max_length=20, default='Closed')

    search_fields = Page.search_fields + [
        index.SearchField('title'),
    ]

    api_fields = [
        APIField('monday'),
        APIField('tuesday'),
        APIField('wednesday'),
        APIField('thursday'),
        APIField('friday'),
        APIField('saturday'),
        APIField('sunday'),
    ]
    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('monday'),
            FieldPanel('tuesday'),
            FieldPanel('wednesday'),
            FieldPanel('thursday'),
            FieldPanel('friday'),
            FieldPanel('saturday'),
            FieldPanel('sunday'),
        ], heading='Working Hours')
    ]

    class Meta:
        verbose_name = 'Opening Hour'
        verbose_name_plural = 'Opening Hours'

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['opening_hours_status'] = WorkingHoursPage.objects.live().exists()
        context['data_exists_status'] = WorkingHoursPage.objects.exists()
        return context
