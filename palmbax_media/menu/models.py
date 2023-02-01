"""Menu Models"""
from django.utils.translation import gettext_lazy as _
from django.db import models

from django_extensions.db.fields import AutoSlugField
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.admin.panels import (
    MultiFieldPanel,
    InlinePanel,
    FieldPanel,
    PageChooserPanel,
    FieldRowPanel,
)
from wagtail.core.models import Orderable
from wagtail.snippets.models import register_snippet
from wagtail.fields import RichTextField

# wagtail API
from wagtail.api import APIField


# Create your models here.


class MenuItem(Orderable):
    link_title = models.CharField(
        blank=True,
        null=True,
        max_length=50
    )
    link_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    link_url = models.CharField(
        max_length=500,
        blank=True
    )
    link_page = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        related_name="+",
        on_delete=models.CASCADE,
    )
    open_in_new_tab = models.BooleanField(default=False, blank=True)

    page = ParentalKey("Menu", related_name="menu_items")

    panels = [
        FieldPanel("link_title"),
        FieldPanel("link_icon"),
        FieldPanel("link_url"),
        PageChooserPanel("link_page"),
        FieldPanel("open_in_new_tab"),
    ]

    @property
    def link(self):
        if self.link_page:
            return self.link_page.url
        elif self.link_url:
            return self.link_url
        return '#'

    @property
    def title(self):
        if self.link_page and not self.link_title:
            return self.link_page.title
        elif self.link_title:
            return self.link_title
        return 'Missing Title'

    """@property
    def title(self):
        if self.link_page and not self.link_title:
            return self.link_page.title.upper()
        elif self.link_title:
            return self.link_title.upper()
        return 'Missing Title'
    """


@register_snippet
class Menu(ClusterableModel):
    """The main menu clusterable model"""

    title = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from="title", editable=True)

    company_name = models.CharField(_('Company Name'),
                                    max_length=50,
                                    default='No Company Name',
                                    null=True,
                                    blank=False,
                                    help_text='Enter company name.')

    company_logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    detail = RichTextField(_('Company detail'),
                           max_length=500,
                           null=True,
                           blank=False,
                           help_text='What is your company?')

    address = models.CharField(_('Address'),
                               max_length=200,
                               null=True,
                               blank=False,
                               help_text='Enter your address.')

    email = models.EmailField(_('Email'),
                              max_length=254,
                              null=True,
                              blank=False,
                              help_text='Enter your email address.')

    phone = models.PositiveSmallIntegerField(_('Phone number'),
                                             null=True,
                                             blank=False,
                                             help_text='Enter your mobile phone number.')

    telephone = models.PositiveSmallIntegerField(_('Telephone number'),
                                                 null=True,
                                                 blank=False,
                                                 help_text='Enter your telephone phone number.')
    # slug = models.SlugField()

    api_fields = [
        APIField('company_name'),
        APIField('company_logo'),
        APIField('detail'),
        APIField('address'),
        APIField('email'),
        APIField('phone'),
        APIField('telephone'),
    ]

    panels = [
        MultiFieldPanel([
            FieldPanel('company_name'),
            FieldPanel('company_logo'),
            FieldPanel('detail'),
            FieldPanel('address'),
            FieldPanel('email'),
            FieldRowPanel([
                FieldPanel('phone', classname='Col6'),
                FieldPanel('telephone', classname='Col6'),
            ]),
        ], heading='Company Information'),
        MultiFieldPanel([
            FieldPanel("title"),
            FieldPanel("slug"),
        ], heading="Menu"),
        InlinePanel("menu_items", label="Menu Item"),
    ]

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menus'
