from django.db import models
# Tools
from django.utils.translation import gettext_lazy as _
from django import forms

# Wagtail
from wagtail.admin.panels import (
    FieldPanel, MultiFieldPanel, InlinePanel, FieldRowPanel
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
        'contact.ContactPage',
        'contact.BookingPage',
        'about.Analytics',
        'about.Clients',
        'about.Testimonials',
    ]

    template = 'about/about_page.html'

    date = models.DateTimeField(auto_now_add=True, null=True)

    about_page_title = models.CharField(_('About Page Subtitle'),
                                        max_length=50,
                                        default='About Page',
                                        null=True,
                                        blank=False,
                                        help_text='This is the About Page.')

    page_description = models.TextField(_('Page Description'),
                                        max_length=500,
                                        null=True,
                                        blank=False,
                                        help_text='Enter any text to describe your page.')

    company_logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    house = models.CharField(_('Building/House #'),
                             max_length=300,
                             null=True,
                             blank=False,
                             help_text='Please enter your building or house number.')

    street = models.CharField(_('Street and Barangay'),
                              max_length=300,
                              null=True,
                              blank=False,
                              help_text='Please enter your company\'s street location and barangay.')

    city = models.CharField(_('City'),
                            max_length=100,
                            null=True,
                            blank=False,
                            help_text='Please enter your company\'s city location.')

    details = RichTextField(_('Company Details'),
                            max_length=1000,
                            blank=True,
                            features=['italic', 'bold'],
                            help_text='Enter your company narrative details.')

    search_fields = Page.search_fields + [
        index.SearchField('about_page_title'),
    ]

    api_fields = [
        APIField('about_page_title'),
        APIField('page_description'),
        APIField('details'),
        APIField('company_logo'),
        APIField('house'),
        APIField('street'),
        APIField('city'),
        APIField('why_choose_us'),
        APIField('about_us_img'),
        APIField('analytics'),
        APIField('clients'),
        APIField('date'),
    ]
    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('about_page_title'),
            FieldPanel('page_description'),
            FieldPanel('company_logo'),
        ], heading='Page Information'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('house', classname="col8"),
                FieldPanel('street', classname="col10"),
                FieldPanel('city', classname="col8"),
            ]),
            FieldPanel('details'),
            InlinePanel('why_choose_us', label='Why choose us'),
            InlinePanel('about_us_img', label='Featured Image(s)'),
        ], heading='About Us Information')
    ]

    class Meta:
        verbose_name = 'About Us Page'
        verbose_name_plural = 'About Us Page'

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

    text = models.TextField(_('Enter your reason'),
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

    date = models.DateTimeField(auto_now_add=True, null=True)

    search_fields = Page.search_fields + [
        index.SearchField('field'),
        index.SearchField('value'),
        index.SearchField('date'),
    ]

    api_fields = [
        APIField('field'),
        APIField('value'),
        APIField('date'),
    ]

    class Meta:
        verbose_name = _('Analytic')
        verbose_name_plural = _('Analytics')

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('field'),
            FieldPanel('value'),
        ], heading='Analytics')
    ]


class Clients(Page):
    """Subpage from about page"""
    template = 'about/clients_page.html'
    parent_page_types = [
        'about.AboutPage',
    ]

    name = models.CharField(_('Client\'s Name'),
                            max_length=50,
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

    date = models.DateTimeField(auto_now_add=True, null=True)

    search_fields = Page.search_fields + [
        index.SearchField('name'),
        index.SearchField('image'),
        index.SearchField('date'),
    ]

    api_fields = [
        APIField('name'),
        APIField('image'),
        APIField('date'),
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


class Testimonials(Page):
    """People will send their testimony from the front end"""
    template = 'about/testimonials_page.html'
    parent_page_types = [
        'about.AboutPage',
    ]

    name = models.CharField(_('Your name'),
                            max_length=50,
                            null=True,
                            blank=False,
                            help_text='Enter the client\'s business name.'
                            )

    profile_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    testimony = models.TextField(_('Testimony'),
                                 max_length=2000,
                                 null=True,
                                 blank=False,
                                 help_text='Input your narrative speech.'
                                 )

    date = models.DateTimeField(auto_now_add=True, null=True)

    search_fields = Page.search_fields + [
        index.SearchField('name'),
    ]

    api_fields = [
        APIField('name'),
        APIField('profile_image'),
        APIField('testimony'),
        APIField('date'),
    ]

    class Meta:
        verbose_name = _('Testimonial')
        verbose_name_plural = _('Testimonials')

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('name'),
            FieldPanel('profile_image'),
            FieldPanel('testimony'),
        ], heading='Testimonial(s)')
    ]
