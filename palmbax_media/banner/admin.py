from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    ModelAdminGroup,
    modeladmin_register
)

from .models import *


class BannerAdmin(ModelAdmin):
    """About admin."""
    model = BannerPage
    base_url_path = 'banner-admin'
    menu_label = 'Banner'  # ditch this to use verbose_name_plural from model
    menu_icon = 'pick'  # change as required
    menu_order = 101  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False  # or True to exclude pages of this type from Wagtail's explorer view
    add_to_admin_menu = True  # or False to exclude your model from the menu
    list_display = ('banner_title', 'description', 'option', 'type', 'date')
    list_filter = ('banner_title', 'option', 'type', 'date')
    search_fields = ('banner_title', 'type', 'date')


modeladmin_register(BannerAdmin)


