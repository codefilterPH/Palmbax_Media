from django.db import models
# Tools
from django.utils.translation import gettext_lazy as _
from django import forms

# Wagtail
from wagtail.admin.panels import (
    FieldPanel, MultiFieldPanel, InlinePanel
)
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.search import index
from modelcluster.fields import ParentalKey
from wagtail.snippets.models import register_snippet

# wagtail API
from wagtail.api import APIField


class AboutPage(Page):
    max_count = 1
    parent_page_types = [
        'home.HomePage',
    ]
    subpage_types = [
        'about.Analytics',
        'about.Clients',
    ]

    template = 'about/about_page.html'
    details = RichTextField(_('Company Details'),
                            max_length=1000,
                            blank=True,
                            features=['italic', 'bold'],
                            help_text='Enter your company narrative details.')

    search_fields = Page.search_fields + [
        index.SearchField('details'),
    ]

    api_fields = [
        APIField('details'),
        APIField('why_choose_us'),
        APIField('about_us_img'),
        APIField('analytics'),
        APIField('clients'),
    ]
    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('details'),
            InlinePanel('why_choose_us', label='Why Choose Us?'),
            InlinePanel('about_us_img', label='Featured Image(s)'),
        ], heading='About Us Information')
    ]

    class Meta:
        verbose_name = 'ABOUT US'
        verbose_name_plural = 'ABOUT US'

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['analytics'] = Analytics.objects.all()
        return context


class WhyChooseUs(Orderable):
    page = ParentalKey(
        'AboutPage',
        on_delete=models.CASCADE,
        related_name='why_choose_us'
    )

    text = models.TextField(_('Why Choose Us?'),
                            null=True,
                            blank=False,
                            help_text='Please enter your reasons.')

    panels = [
        FieldPanel('text'),
    ]

    class Meta:
        verbose_name = 'WHY CHOOSE US?'
        verbose_name_plural = 'WHY CHOOSE US?'


class AboutUsImage(Orderable):
    page = ParentalKey(
        'AboutPage',
        on_delete=models.CASCADE,
        related_name='about_us_img',
    )

    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        FieldPanel('image')
    ]

    class Meta:
        verbose_name = 'Featured Image'
        verbose_name_plural = 'Featured Images'


class Analytics(Page):
    """Subpage from about page"""
    template = 'analytics_page.html'
    parent_page_types = [
        'about.AboutPage',
    ]

    value = models.PositiveSmallIntegerField(_('Analytic Value'),
                                             null=True,
                                             blank=False,
                                             help_text='Enter the whole number value 1-100+'
                                             )
    field = models.CharField(_('Field Name'),
                             max_length=40,
                             null=True,
                             blank=False,
                             help_text='Enter the field name. ex: \"Number of clients\".')

    search_fields = Page.search_fields + [
        index.SearchField('value'),
        index.SearchField('field'),
    ]

    api_fields = [
        APIField('value'),
        APIField('field'),
    ]

    class Meta:
        verbose_name = _('Analytic')
        verbose_name_plural = _('Analytics')

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('value'),
            FieldPanel('field'),
        ], heading='Analytics')
    ]


class Clients(Page):
    """Subpage from about page"""
    template = 'about/clients_page.html'
    parent_page_types = [
        'about.AboutPage',
    ]

    name = models.CharField(_('Client\'s Name'),
                            max_length=40,
                            null=True,
                            blank=False,
                            help_text='Enter the client\'s business name.'
                            )

    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    search_fields = Page.search_fields + [
        index.SearchField('name'),
        index.SearchField('image'),
    ]

    api_fields = [
        APIField('name'),
        APIField('image'),
    ]

    class Meta:
        verbose_name = _('Client')
        verbose_name_plural = _('Clients')

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('name'),
            FieldPanel('image'),
        ], heading='Clients')
    ]