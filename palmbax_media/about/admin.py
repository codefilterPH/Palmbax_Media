from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    ModelAdminGroup,
    modeladmin_register
)

from .models import *


class AboutAdmin(ModelAdmin):
    """About admin."""
    model = AboutPage
    base_url_path = 'about-model-admin'
    menu_label = 'About'  # ditch this to use verbose_name_plural from model
    menu_icon = 'pick'  # change as required
    menu_order = 100  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False  # or True to exclude pages of this type from Wagtail's explorer view
    add_to_admin_menu = True  # or False to exclude your model from the menu
    list_display = ('about_page_title', 'page_description', 'date')
    list_filter = ('about_page_title', 'date')
    search_fields = ('about_page_title',)


class AnalyticAdmin(ModelAdmin):
    """About analytic admin."""
    model = Analytics
    base_url_path = 'about-analytics-admin'
    menu_label = 'Analytics'  # ditch this to use verbose_name_plural from model
    menu_icon = 'pick'  # change as required
    menu_order = 100  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False  # or True to exclude pages of this type from Wagtail's explorer view
    add_to_admin_menu = True  # or False to exclude your model from the menu
    list_display = ('field', 'value', 'date')
    list_filter = ('field', 'value', 'date')
    search_fields = ('field', 'value', 'date')


class ClientAdmin(ModelAdmin):
    """About analytic admin."""
    model = Clients
    base_url_path = 'about-clients-admin'
    menu_label = 'Client(s)'  # ditch this to use verbose_name_plural from model
    menu_icon = 'pick'  # change as required
    menu_order = 100  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False  # or True to exclude pages of this type from Wagtail's explorer view
    add_to_admin_menu = True  # or False to exclude your model from the menu
    list_display = ('name', 'image', 'date')
    list_filter = ('name', 'image', 'date')
    search_fields = ('name', 'date')


class TestimonialAdmin(ModelAdmin):
    """About analytic admin."""
    model = Testimonials
    base_url_path = 'about-testimonial-admin'
    menu_label = 'Testimonial(s)'  # ditch this to use verbose_name_plural from model
    menu_icon = 'pick'  # change as required
    menu_order = 100  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False  # or True to exclude pages of this type from Wagtail's explorer view
    add_to_admin_menu = True  # or False to exclude your model from the menu
    list_display = ('name', 'profile_image', 'testimony', 'date')
    list_filter = ('name', 'date')
    search_fields = ('name', 'date')


class TestimonialGroupAdmin(ModelAdminGroup):
    menu_label = 'About'
    menu_icon = 'folder-open-inverse'  # change as required
    menu_order = 102  # will put in 3rd place (000 being 1st, 100 2nd)
    items = (AboutAdmin, AnalyticAdmin, ClientAdmin, TestimonialAdmin)


modeladmin_register(TestimonialGroupAdmin)
