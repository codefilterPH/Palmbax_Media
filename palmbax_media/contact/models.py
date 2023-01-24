from django.db import models
# Tools
from django.utils.translation import gettext_lazy as _
# Wagtail
from wagtail.admin.panels import (
    FieldPanel, FieldRowPanel, MultiFieldPanel, InlinePanel
)
from wagtail.models import Page, Orderable
from wagtail.search import index
from modelcluster.fields import ParentalKey
from wagtail.core.fields import RichTextField

# Wagtail Api
from wagtail.api import APIField

# Submission Form
from wagtail.contrib.forms.models import (
    AbstractEmailForm,
    AbstractFormField
)
from about.models import *

# third party
import folium
import geocoder


class ContactFormField(AbstractFormField):
    page = ParentalKey(
        'ContactPage',
        on_delete=models.CASCADE,
        related_name='form_fields',
    )


class ContactPage(AbstractEmailForm):
    max_count = 1
    parent_page_types = [
        'about.AboutPage',
    ]
    template = 'contact/contact_page.html'
    landing_page_template = "contact/contact_page_landing.html"

    date = models.DateTimeField(auto_now_add=True, null=True)

    contact_page_title = models.CharField(_('Contact Page Subtitle'),
                                          max_length=50,
                                          default='Contact Page',
                                          null=True,
                                          blank=False,
                                          help_text='This is the Contact Page.')

    page_description = models.TextField(_('Page Description'),
                                        max_length=500,
                                        null=True,
                                        blank=False,
                                        help_text='Enter any text to describe your page.')

    contact_thank_you_text = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel('contact_page_title'),
        FieldPanel('page_description'),
        MultiFieldPanel([
            InlinePanel('form_fields', label='Form Fields'),
            FieldPanel('contact_thank_you_text'),
            MultiFieldPanel([
                FieldRowPanel([
                    FieldPanel('from_address', classname="col6"),
                    FieldPanel('to_address', classname="col6"),
                ]),
                FieldPanel("subject"),
            ], heading="Email Settings"),
        ], heading="Contact Page Form"),
    ]

    class Meta:
        verbose_name = _('Contact Page')
        verbose_name_plural = _('Contact Page')

    def get_context(self, request, *args, **kwargs):
        address = AboutPage.objects.values_list('city')

        location = geocoder.osm(address)
        latitude = location.lat
        longitude = location.lng
        country = location.country

        # generate map
        my_map = folium.Map(location=[latitude, longitude],
                            tiles='openstreetmap',
                            zoom_start=10,
                            control_scale=True)
        folium.Marker([latitude, longitude],
                      tooltip=country,
                      popup=f'<p id="latlon">{latitude}, {longitude}</p>', ).add_to(my_map)
        my_map.add_child(folium.LatLngPopup())

        context = super().get_context(request, *args, **kwargs)
        # Get representation of map objects
        context['my_map'] = my_map._repr_html_()
        context['address'] = address
        context['country'] = country
        context['contact_data'] = ContactPage.objects.all()

        return context


class BookingFormField(AbstractFormField):
    page = ParentalKey(
        'BookingPage',
        on_delete=models.CASCADE,
        related_name='form_fields',
    )


class BookingPage(AbstractEmailForm):
    max_count = 1
    parent_page_types = [
        'about.AboutPage',
    ]
    template = 'book/book_page.html'
    landing_page_template = "book/book_page_landing.html"

    date = models.DateTimeField(auto_now_add=True, null=True)

    book_page_title = models.CharField(_('Booking Page Subtitle'),
                                       max_length=50,
                                       default='Booking Page',
                                       null=True,
                                       blank=False,
                                       help_text='This is the Contact Page.')

    page_description = models.TextField(_('Page Description'),
                                        max_length=500,
                                        null=True,
                                        blank=False,
                                        help_text='Enter any text to describe your page.')

    book_thank_you_text = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel('book_page_title'),
        FieldPanel('page_description'),
        MultiFieldPanel([
            InlinePanel('form_fields', label='Form Fields'),
            FieldPanel('book_thank_you_text'),
            MultiFieldPanel([
                FieldRowPanel([
                    FieldPanel('from_address', classname="col6"),
                    FieldPanel('to_address', classname="col6"),
                ]),
                FieldPanel("subject"),
            ], heading="Email Settings"),
        ], heading="Booking Page Form"),
    ]

    class Meta:
        verbose_name = _('Booking Page')
        verbose_name_plural = _('Booking Pages')

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['booking_data'] = BookingPage.objects.all()

        return context
