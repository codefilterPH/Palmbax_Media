from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    ModelAdminGroup,
    modeladmin_register
)

from .models import *


class ServicesAdmin(ModelAdmin):
    """About admin."""
    model = ServicesPage
    base_url_path = 'services-page-list'
    menu_label = 'Services Offered'  # ditch this to use verbose_name_plural from model
    menu_icon = 'pick'  # change as required
    menu_order = 102  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False  # or True to exclude pages of this type from Wagtail's explorer view
    add_to_admin_menu = True  # or False to exclude your model from the menu
    list_display = ('title', 'description', 'live', 'first_published_at', 'last_published_at')
    list_filter = ('title', 'description', 'live', 'first_published_at', 'last_published_at')
    search_fields = ('title', 'description',)


modeladmin_register(ServicesAdmin)


class ServicesGroupAdmin(ModelAdminGroup):
    menu_label = 'Services'
    menu_icon = 'folder-open-inverse'  # change as required
    menu_order = 103  # will put in 3rd place (000 being 1st, 100 2nd)
    items = (ServicesAdmin,)


