from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea, NumberInput
from estateobjects.models import Contact, Store, Bid, Image, EstateObject

from ordered_model.admin import OrderedTabularInline, OrderedInlineModelAdminMixin, OrderedModelAdmin

class ImageInline(OrderedTabularInline):
    model = Image
    fields = ('image', 'move_up_down_links',)
    readonly_fields = ('move_up_down_links',)
    ordering = ('order',)
    extra = 1

class EstateObjectAdmin(OrderedInlineModelAdminMixin, OrderedModelAdmin):
    model = EstateObject

    inlines = ( ImageInline, )

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

    list_display = ('collection_id', 'title', 'creation_year',
                    'reserved_for',  'move_up_down_links', 'order')

admin.site.register(Contact)
admin.site.register(Store)
admin.site.register(Bid)
admin.site.register(EstateObject, EstateObjectAdmin)
