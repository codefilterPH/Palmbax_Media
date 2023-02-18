from django.db import models
from menu.models import *
from wagtail.models import Page
from about.models import *
from services.models import *
from working_hours.models import *
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from contact.models import *
from menu.models import *
from booking.models import *


class HomePage(Page):
    max_count = 1
    template = 'home/home_page.html'
    subpage_types = [
        'about.AboutPage',
        'working_hours.WorkingHoursPage',
        'contact.ContactPage',
        'banner.BannerPage',
        'services.ServicePage',
        'booking.BookingPage',
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
        # Contact Page
        context['contact_page_status'] = ContactPage.objects.live().exists()
        context['contact_page'] = ContactPage.objects.live().first()
        address = Menu.objects.values_list('address', flat=True).first()
        if BookingPage.objects.live().exists():
            booking_page = BookingPage.objects.live().first()
            context['book_page'] = booking_page.url

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
                context['address'] = address

            except:
                context['address'] = address + 'Return a status of \"Invalid address or not found!\" try changing it.'

        return context
