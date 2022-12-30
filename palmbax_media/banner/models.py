from django.db import models
# Tool
from django.utils.translation import gettext_lazy as _

# Wagtail
from wagtail.admin.panels import (
    FieldPanel, MultiFieldPanel, InlinePanel
)
from wagtail.models import Page, Orderable
from wagtail.search import index
# Wagtail Api
from wagtail.api import APIField
# Create your models here.


class Banner(Page):
    parent_page_types = [
        'home.HomePage',
    ]
    template = 'about/about_page.html'

