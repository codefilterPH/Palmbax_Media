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
from menu.models import *

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
        'home.HomePage',
    ]
    template = 'contact/contact_page.html'
    landing_page_template = "contact/contact_page_landing.html"
    contact_thank_you_text = RichTextField(blank=True, default='Thank you for contacting us! We\'ll get back to you '
                                                               'shortly.')

    content_panels = AbstractEmailForm.content_panels + [
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
        address = Menu.objects.values_list('address')

        location = geocoder.osm(address)
        latitude = location.lat
        longitude = location.lng
        country = location.country

        # generate map
        my_map = folium.Map(location=[latitude, longitude],
                            tiles='openstreetmap',
                            zoom_start=15,
                            control_scale=True)
        folium.Marker([latitude, longitude],
                      tooltip=country,
                      popup=f'<p id="latlon">{latitude}, {longitude}</p>', ).add_to(my_map)
        my_map.add_child(folium.LatLngPopup())

        context = super().get_context(request, *args, **kwargs)
        # Get representation of map objects
        context['my_map'] = my_map._repr_html_()
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
    book_thank_you_text = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
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
