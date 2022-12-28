from django.db import models
# Tools
from django.utils.translation import gettext_lazy as _
from django import forms
from wagtail.admin.panels import FieldPanel, MultiFieldPanel

# Wagtail
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.search import index
from modelcluster.fields import ParentalKey

#wagtail API
from wagtail.api import APIField

class AboutPage(Page):
    parent_page_types = [
        'home.HomePage',
    ]
    template = 'about/about_page.html'
    details = RichTextField(_('Company Details'),
                            max_length=1000,
                            blank=False,
                            features=['italic', 'bold'],
                            help_text='Enter your company narrative details.')

    search_fields = Page.search_fields + [
        index.SearchField('details'),
    ]

    api_fields = [
        APIField('details'),
    ]
    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('details'),
        ],heading='About Us Information')
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        return context

    class Meta:
        verbose_name = 'ABOUT US'
        verbose_name_plural = 'ABOUT US'

class WhyChooseUs(Orderable):
    page = ParentalKey(
        'AboutPage',
        on_delete=models.CASCADE,
        related_name='why_choose_us'
    )



