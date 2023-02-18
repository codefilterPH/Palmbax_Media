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
        limit_choices_to={'live': True},
        help_text='Select only a lived or published page',
    )
    open_in_new_tab = models.BooleanField(default=False, blank=True)

    page = ParentalKey("Menu", related_name="menu_items")

    panels = [
        FieldPanel("link_title"),
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

    title = models.CharField(max_length=100,
                             default='Main-Menu')
    slug = AutoSlugField(populate_from="title",
                         editable=True,
                         default='main-menu')

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

    COLOR_CHOICES = [
        ('#ffffff', 'Light'),
        ('#007bff', 'Blue'),
        ('#37a1fe', 'Sky Blue'),
        ('#4caf50', 'Green'),
        ('#7f00ff', 'Purple'),
        ('#3c3c3c', 'Dark'),
        ('#000000', 'Black'),

    ]
    bg_color = models.CharField(_('Background Color'),
                                max_length=7,
                                choices=COLOR_CHOICES,
                                default='#ffffff',
                                )
    GRADIANT_CHOICES = [
        ('linear-gradient(135deg, #C33764 10%, #1D2671 100%)', 'Dark Purple Blue'),
        ('linear-gradient(135deg, #92FFC0 10%, #002661 100%)', 'Aqua Blue'),
        ('linear-gradient(135deg, #536976 10%, #292E49 100%)', 'Light Dark'),
        ('linear-gradient(135deg, #FFDB01 10%, #0E197D 100%)', 'Gold Blue'),
        ('linear-gradient(135deg, #FF9D6C 10%, #BB4E75 100%)', 'BRT Orange & Mod Pink'),
        ('linear-gradient(135deg, #007adf 10%, #00ecbc 100%)', 'Dark Sky Blue'),
        ('linear-gradient(135deg, #434343 10%, #000000 100%)', 'Dark Grey'),

    ]
    bg_gradiant_image = models.CharField(_('Background Gradiant Color'),
                                         max_length=50,
                                         choices=GRADIANT_CHOICES,
                                         default='linear-gradient(135deg, #434343 10%, #000000 100%)',
                                         )

    bg_color_settings = models.BooleanField(_('Use Gradient as Background'), default=False)

    font_color = models.CharField(_('Font Color'),
                                  max_length=7,
                                  choices=COLOR_CHOICES,
                                  default='#ffffff',
                                  )
    FONT_CHOICES = [
        ("Sofia Sans, sans-serif", "Sofia Sans"),
        ("Open Sans, sans-serif", "Open Sans"),
        ("Quicksand, sans-serif", "Quicksand"),
        ("none", "None"),
    ]

    font = models.CharField(_("Font Family"),
                            max_length=50,
                            choices=FONT_CHOICES,
                            default="Sofia Sans, sans-serif",
                            )
    fb_profile = models.CharField(_('Facebook Profile'),
                                  max_length=500,
                                  blank=True,
                                  help_text='Ex. https://www.facebook.com/codefilterph'
                                  )
    twitter_profile = models.CharField(_('Twitter Profile'),
                                       max_length=500,
                                       blank=True
                                       )
    gmail_profile = models.CharField(_('Gmail Profile'),
                                     max_length=500,
                                     blank=True
                                     )
    instagram_profile = models.CharField(_('Instagram Profile'),
                                         max_length=500,
                                         blank=True
                                         )
    linked_profile = models.CharField(_('Linkedin Profile'),
                                      max_length=500,
                                      blank=True
                                      )

    # slug = models.SlugField()

    api_fields = [
        APIField('company_name'),
        APIField('company_logo'),
        APIField('detail'),
        APIField('address'),
        APIField('email'),
        APIField('phone'),
        APIField('telephone'),
        APIField('bg_color'),
        APIField('bg_gradiant_image'),
        APIField('bg_color_settings'),
        APIField('font_color'),
        APIField('font'),
    ]

    panels = [
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('font_color', classname='Col2'),
                FieldPanel('font', classname='Col6'),
            ]),
            FieldRowPanel([
                FieldPanel('bg_color', classname='Col4'),
                FieldPanel('bg_gradiant_image', classname='Col4'),
                FieldPanel('bg_color_settings', classname='Col2'),
            ])
        ], heading='Theme'),
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
            MultiFieldPanel([
                FieldPanel('fb_profile'),
                FieldPanel('twitter_profile'),
                FieldPanel('gmail_profile'),
                FieldPanel('instagram_profile'),
                FieldPanel('linked_profile'),
            ], heading = 'Social Media Accounts'),
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
        verbose_name = 'Main Setup'
        verbose_name_plural = 'Main Setup'

