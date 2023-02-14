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
from django.core.mail import EmailMessage

from menu.models import *

# third party
import folium
import geopy
from geopy.geocoders import Nominatim


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

    search_fields = Page.search_fields + [
        index.SearchField('title'),
    ]

    class Meta:
        verbose_name = _('Contact Page')
        verbose_name_plural = _('Contact Page')

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        # Retrieve address value from database
        address = Menu.objects.values_list('address', flat=True).first()

        # If address is not None, get the location information
        if address is not None:
            geolocator = Nominatim(user_agent="Corporate Website")
            location = geolocator.geocode(address)

            # Generate map
            try:
                latitude = location.latitude
                longitude = location.longitude
                my_map = folium.Map(location=[latitude, longitude],
                                    tiles='openstreetmap',
                                    zoom_start=15,
                                    control_scale=True)
                folium.Marker([latitude, longitude],
                              tooltip=address,
                              popup=f'<p id="latlon">{latitude}, {longitude}</p>').add_to(my_map)
                my_map.add_child(folium.LatLngPopup())
                # Add map and contact data to context
                context['my_map'] = my_map._repr_html_()
                context['contact_page_status'] = ContactPage.objects.live().exists()
                context['address'] = address
            except:
                context['contact_page_status'] = ContactPage.objects.live().exists()
                context['address'] = address + 'Return a status of \"Invalid address or not found!\" try changing it.'

        return context

    def process_form_submission(self, form):
        # Call the parent class's method to handle the form submission
        super().process_form_submission(form)

        # Get the form data
        data = form.cleaned_data
        email = Menu.objects.values_list('email', flat=True).first()
        # Construct the email message
        subject = self.subject
        body = '\n'.join([f'{key}: {value}' for key, value in data.items()])
        from_email = email
        to_email = self.to_address
        email_message = EmailMessage(subject, body, from_email, [to_email])

        # Send the email
        email_message.send()
