from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    ModelAdminGroup,
    modeladmin_register
)

from .models import *


class ServicesAdmin(ModelAdmin):
    """About admin."""
    model = ServicesPage
    base_url_path = 'services-model-admin'
    menu_label = 'Services Offered'  # ditch this to use verbose_name_plural from model
    menu_icon = 'pick'  # change as required
    menu_order = 100  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False  # or True to exclude pages of this type from Wagtail's explorer view
    add_to_admin_menu = True  # or False to exclude your model from the menu
    list_display = ('services_page_title', 'page_description', 'date')
    list_filter = ('services_page_title', 'date')
    search_fields = ('services_page_title',)


class ServicesGroupAdmin(ModelAdminGroup):
    menu_label = 'Services'
    menu_icon = 'folder-open-inverse'  # change as required
    menu_order = 103  # will put in 3rd place (000 being 1st, 100 2nd)
    items = (ServicesAdmin,)


modeladmin_register(ServicesGroupAdmin)