from django.db import models

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

    intro = RichTextField(blank=True)
    contact_thank_you_text = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel('intro'),
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
        ], heading="Contact Form"),
    ]

    class Meta:
        verbose_name = 'Contact Page'
        verbose_name_plural = 'Contact Page'

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
        context['contact_form'] = ContactPage.objects.all()

        return context
