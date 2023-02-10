from django.db import models
from menu.models import *
from wagtail.models import Page
from about.models import *
from services.models import *
from working_hours.models import *


class HomePage(Page):
    max_count = 1
    template = 'home/home_page.html'
    subpage_types = [
        'about.AboutPage',
        'working_hours.WorkingHoursPage',
        'contact.ContactPage',
        'banner.BannerPage',
        'services.ServicesPage'
    ]

    def __str__(self):
        return self.title

    class Meta:
        verbose_name: 'Home'
        verbose_name_plural = 'Home'

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['about_page'] = AboutPage.objects.live()
        context['live_page_status'] = AboutPage.objects.live().exists()

        return context
