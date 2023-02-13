from django.db import models
from menu.models import *
from wagtail.models import Page
from about.models import *
from services.models import *
from working_hours.models import *
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


class HomePage(Page):
    max_count = 1
    template = 'home/home_page.html'
    subpage_types = [
        'about.AboutPage',
        'working_hours.WorkingHoursPage',
        'contact.ContactPage',
        'banner.BannerPage',
        'services.ServicePage',
    ]

    def __str__(self):
        return self.title

    class Meta:
        verbose_name: 'Home'
        verbose_name_plural = 'Home'

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['about_page_status'] = AboutPage.objects.live().exists()
        context['about_page'] = AboutPage.objects.live()
        context['people_live_status'] = PeoplePage.objects.filter(feature=1).live().exists()
        all_people = PeoplePage.objects.filter(feature=1).live()
        paginator = Paginator(all_people, 3)
        page = request.GET.get("page")
        try:
            context['people'] = paginator.page(page)
        except PageNotAnInteger:
            context['people'] = paginator.page(1)
        except EmptyPage:
            context['people'] = paginator.page(paginator.num_pages)

        context['services_page_status'] = ServiceDetailPage.objects.filter(feature=1).live().exists()
        all_pages = ServiceDetailPage.objects.filter(feature=1).live()
        paginator = Paginator(all_pages, 3)
        page = request.GET.get("page")
        try:
            context['service_data'] = paginator.page(page)
        except PageNotAnInteger:
            context['service_data'] = paginator.page(1)
        except EmptyPage:
            context['service_data'] = paginator.page(paginator.num_pages)

        context['opening_hours_status'] = WorkingHoursPage.objects.live().exists()
        context['opening_hours'] = WorkingHoursPage.objects.live()
        return context
