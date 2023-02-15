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


class BookingFormField(AbstractFormField):
    page = ParentalKey(
        'BookingPage',
        on_delete=models.CASCADE,
        related_name='form_fields',
    )


class BookingPage(AbstractEmailForm):
    max_count = 1
    parent_page_types = [
        'home.HomePage',
    ]
    template = 'booking/book_page.html'
    landing_page_template = "booking/book_page_landing.html"
    book_thank_you_text = RichTextField(blank=True)

    booking_page_background = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Best size will be 1920x1080 pixels.'
    )

    booking_cover_settings = models.BooleanField(_('Use Default Background Image'),
                                            default=True,
                                            help_text='Do you want to use the default parallax cover image? click the '
                                                      'box for yes.')

    content_panels = AbstractEmailForm.content_panels + [
        MultiFieldPanel([
            FieldPanel('booking_page_background'),
            FieldPanel('booking_cover_settings'),
        ], heading='Page Setup'),
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
        context['booking_page_status'] = BookingPage.objects.live().exists()

        return context
