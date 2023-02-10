from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    ModelAdminGroup,
    modeladmin_register
)

from .models import *


class OpeningHoursAdmin(ModelAdmin):
    """About admin."""
    model = WorkingHoursPage
    base_url_path = 'opening-hours'
    menu_label = 'Opening Hours'  # ditch this to use verbose_name_plural from model
    menu_icon = 'pick'  # change as required
    menu_order = 102  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False  # or True to exclude pages of this type from Wagtail's explorer view
    add_to_admin_menu = True  # or False to exclude your model from the menu
    list_display = ('title', 'live', 'first_published_at', 'last_published_at')
    list_filter = ('title', 'live', 'first_published_at', 'last_published_at')
    search_fields = ('title',)


modeladmin_register(OpeningHoursAdmin)
