from django.db import models
# Tools
from django.utils.translation import gettext_lazy as _
from django import forms

# Wagtail
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField

class AboutPage(Page):
    parent_page_types = [
        'home.HomePage',
    ]

