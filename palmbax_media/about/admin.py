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


class AnalyticIndexAdmin(ModelAdmin):
    """About analytic admin."""
    model = AnalyticSettings
    base_url_path = 'about-analytics-setup'
    menu_label = 'Analytics Setup'  # ditch this to use verbose_name_plural from model
    menu_icon = 'pick'  # change as required
    menu_order = 100  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False  # or True to exclude pages of this type from Wagtail's explorer view
    add_to_admin_menu = True  # or False to exclude your model from the menu
    list_display = ('analytics_background_img',)


class AnalyticAdmin(ModelAdmin):
    """About analytic admin."""
    model = Analytics
    base_url_path = 'about-analytics'
    menu_label = 'Analytic Entries'  # ditch this to use verbose_name_plural from model
    menu_icon = 'pick'  # change as required
    menu_order = 100  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False  # or True to exclude pages of this type from Wagtail's explorer view
    add_to_admin_menu = True  # or False to exclude your model from the menu
    list_display = ('field', 'value', 'live', 'first_published_at', 'last_published_at')
    list_filter = ('field', 'value', 'live', 'first_published_at', 'last_published_at')
    search_fields = ('field', 'value')


class ClientAdmin(ModelAdmin):
    """About analytic admin."""
    model = Clients
    base_url_path = 'about-clients'
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
    base_url_path = 'about-testimonial'
    menu_label = 'Testimonial(s)'  # ditch this to use verbose_name_plural from model
    menu_icon = 'pick'  # change as required
    menu_order = 100  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False  # or True to exclude pages of this type from Wagtail's explorer view
    add_to_admin_menu = True  # or False to exclude your model from the menu
    list_display = ('name', 'profile_image', 'testimony', 'date')
    list_filter = ('name', 'date')
    search_fields = ('name', 'date')


class AboutGroupAdmin(ModelAdminGroup):
    menu_label = 'About'
    menu_icon = 'folder-open-inverse'  # change as required
    menu_order = 102  # will put in 3rd place (000 being 1st, 100 2nd)
    items = (AboutAdmin, AnalyticIndexAdmin, AnalyticAdmin, ClientAdmin, TestimonialAdmin)


modeladmin_register(AboutGroupAdmin)
