from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    ModelAdminGroup,
    modeladmin_register
)

from .models import *


class ContactAdmin(ModelAdmin):
    """Contact Page admin."""
    model = ContactPage
    base_url_path = 'contact-model-admin'
    menu_label = 'Contact Page'  # ditch this to use verbose_name_plural from model
    menu_icon = 'pick'  # change as required
    menu_order = 100  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False  # or True to exclude pages of this type from Wagtail's explorer view
    add_to_admin_menu = True  # or False to exclude your model from the menu
    list_display = ('contact_page_title', 'page_description', 'date')
    list_filter = ('contact_page_title', 'date')
    search_fields = ('contact_page_title',)


class BookingAdmin(ModelAdmin):
    """Booking Page admin."""
    model = BookingPage
    base_url_path = 'booking-model-admin'
    menu_label = 'Booking Page'  # ditch this to use verbose_name_plural from model
    menu_icon = 'pick'  # change as required
    menu_order = 100  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False  # or True to exclude pages of this type from Wagtail's explorer view
    add_to_admin_menu = True  # or False to exclude your model from the menu
    list_display = ('book_page_title', 'page_description', 'date')
    list_filter = ('book_page_title', 'date')
    search_fields = ('book_page_title',)


class ContactGroupAdmin(ModelAdminGroup):
    menu_label = 'Contact'
    menu_icon = 'folder-open-inverse'  # change as required
    menu_order = 103  # will put in 3rd place (000 being 1st, 100 2nd)
    items = (ContactAdmin, BookingAdmin,)


modeladmin_register(ContactGroupAdmin)