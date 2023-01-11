from django.db import models
from django.http import HttpResponse
# Wagtail
from wagtail.admin.panels import (
    FieldPanel, MultiFieldPanel, InlinePanel
)
from wagtail.models import Page, Orderable
from wagtail.search import index
from modelcluster.fields import ParentalKey
# Wagtail Api
from wagtail.api import APIField

from about.models import *

# third party
import folium
import geocoder


class ContactPage(Page):
    parent_page_types = [
        'home.HomePage',
    ]
    template = 'contact/contact_page.html'

    class Meta:
        verbose_name = 'Contact Page'
        verbose_name_plural = 'Contact Pages'

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        address = AboutPage.objects.values_list('address')

        location = geocoder.osm(address)
        latitude = location.lat
        longitude = location.lng
        country = location.country

        # generate map
        my_map = folium.Map(location=[latitude, longitude],
                            tiles='openstreetmap',
                            zoom_start=17,
                            control_scale=True)
        folium.Marker([latitude, longitude],
                      tooltip=country,
                      popup=f'<p id="latlon">{latitude}, {longitude}</p>', ).add_to(my_map)
        my_map.add_child(folium.LatLngPopup())
        # Get representation of map objects
        context['my_map'] = my_map._repr_html_()
        context['address'] = address
        context['country'] = country

        return context

