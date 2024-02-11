from django.utils.translation import gettext as _, gettext_lazy

from cms.toolbar_base import CMSToolbar
from cms.toolbar_pool import toolbar_pool
from cms.utils.urlutils import admin_reverse

@toolbar_pool.register
class EstateobjectsToolbar(CMSToolbar):
    def populate(self):
        menu = self.toolbar.get_or_create_menu(
            'estateobjects_menu',  # a unique key for this menu
            'Estate',                        # the text that should appear in the menu
            )
        menu.add_sideframe_item(
            name=_("Estate objects"),
            url=admin_reverse("estateobjects_estateobject_changelist")
        )
        menu.add_sideframe_item(
            name=_("Bids"),
            url=admin_reverse("estateobjects_bid_changelist")
        )
        menu.add_sideframe_item(
            name=_("Contacts"),
            url=admin_reverse("estateobjects_contact_changelist")
        )
        menu.add_sideframe_item(
            name=_("Stores"),
            url=admin_reverse("estateobjects_store_changelist")
        )
