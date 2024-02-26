from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea, NumberInput
from cms.admin.placeholderadmin import FrontendEditableAdminMixin
from estateobjects.models import Contact, Store, Bid, Image, EstateObject

from ordered_model.admin import OrderedTabularInline, OrderedInlineModelAdminMixin, OrderedModelAdmin

class ImageInline(OrderedTabularInline):
    model = Image
    fields = ('image', 'move_up_down_links',)
    readonly_fields = ('move_up_down_links',)
    ordering = ('order',)
    extra = 0

class BidInline(admin.TabularInline):
    model = Bid
    readonly_fields = ('created_at', )
    fields = ('created_at', 'bidder', 'price')
    ordering = ('created_at', )
    extra = 0

class EstateObjectAdmin(FrontendEditableAdminMixin, OrderedInlineModelAdminMixin, OrderedModelAdmin):
    model = EstateObject

    inlines = ( BidInline, ImageInline, )

    fields = [ ('title', 'collection_id'),
               ('creation_year', 'creation_month'),
               ('sale_date', 'sale_price'),
               ('asking_price', 'depth_cm'),
               ('height_cm', 'width_cm'),
               ('object_type', 'object_material'),
               ('object_state' ,'store' ),
               ('owner', 'reserved_for'),
               'description',
    ]

    list_display = ('collection_id', 'title', 'creation_year', 'creation_month',
                    'description', 'store', 'height_cm', 'object_type', 'object_state',
                    'reserved_for', 'owner', 'move_up_down_links')

    list_filter = ('creation_year',
                   'store', 'object_type', 'object_state',
                   'reserved_for', 'owner', 'image')

admin.site.register(Contact)
admin.site.register(Store)
admin.site.register(Bid)
admin.site.register(EstateObject, EstateObjectAdmin)
