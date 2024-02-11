# from django.db import models
from django.contrib.gis.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator 
from django.utils.translation import gettext as _

from filer.fields.image import FilerImageField
from ordered_model.models import OrderedModel

# User = get_user_model()

class Contact(models.Model):
    name = models.CharField(max_length=512)
    email_address = models.CharField(max_length=512)
    post_address = models.TextField(blank=True)
    phone_number = models.CharField(max_length=512, blank=True)

    def __str__(self):
        return self.name

class Store(models.Model):
    """A physical container that stores estate objects or other stores."""
    class StoreType(models.TextChoices):
        BOX = "BO", _("Box")
        ROOM = "RO", _("Room")
        BUILDING = "BU", _("Building")
        OUTSIDE = "OU", _("Outside")
    
    name = models.CharField(max_length=512)
    collection_id = models.IntegerField(blank=True, null=True, unique=True)
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.RESTRICT)
    # position = models.PointField(blank=True, null=True)
    address = models.TextField(blank=True)
    store_type = models.CharField(max_length=2, choices=StoreType)

    def __str__(self):
        return f'[{Store.StoreType(self.store_type).name.title()}] {self.name}'


class Bid(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    bidder = models.ForeignKey(Contact, blank=True, null=True, on_delete=models.RESTRICT)
    estate_object = models.ForeignKey('EstateObject', on_delete=models.RESTRICT)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f'{self.estate_object} - {self.bidder} @ {self.price} €'


class Image(OrderedModel):
    estate_onject = models.ForeignKey('EstateObject', on_delete=models.RESTRICT)
    image = FilerImageField(on_delete=models.CASCADE)
    

class EstateObject(OrderedModel):
    title = models.CharField(blank=True, max_length=512)
    collection_id = models.IntegerField()

    creation_year = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1950), MaxValueValidator(2012)])
    creation_month = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(12)])

    sale_date = models.DateField(blank=True, null=True)
    sale_price = models.DecimalField(blank=True, null=True, max_digits=8, decimal_places=2)

    asking_price = models.DecimalField(blank=True, null=True, max_digits=8, decimal_places=2)
    
    width_cm = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(0), MaxValueValidator(1000)])
    height_cm = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(0), MaxValueValidator(1000)])
    depth_cm = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(0), MaxValueValidator(1000)])

    store = models.ForeignKey('Store', blank=True, null=True, on_delete=models.RESTRICT)
    
    owner = models.ForeignKey(Contact, blank=True, null=True, on_delete=models.RESTRICT, related_name="owner")
    reserved_for = models.ForeignKey(Contact, blank=True, null=True, on_delete=models.RESTRICT, related_name="reserved_for")

    description = models.TextField(blank=True)

    class EstateObjectType(models.TextChoices):
        SCULPTURE = "SC", _("Sculpture")
        PAINTING = "PA", _("Painting")
        DRAWING = "DR", _("Drawing")
        OTHER = "OT", _("Other")

    object_type = models.CharField(blank=True, max_length=2, choices=EstateObjectType)

    class Material(models.TextChoices):
        STEEL = "ST", _("Steel")
        BRONZE = "BR", _("Bronze")
        WOOD = "WO", _("Wood")
        PAPER = "PA", _("Paper")
        MIXED = "MI", _("Mixed")
        OTHER = "OT", _("Other")

    object_material = models.CharField(blank=True, max_length=2, choices=Material)

    class State(models.TextChoices):
        PERFECT = "PE", _("Perfect")
        SLIGHTLY_DETERIORATED = "SD", _("Slightly deteriorated")
        NEED_RESTORATION = "RE", _("Needs restoration")
        NON_RESTORABLE = "NR", _("Non restorable")
    
    object_state = models.CharField(blank=True, max_length=2, choices=State)

    def image_main(self):
        first = self.image_set.first()
        if first:
            print('first', first.image)
            return first.image

    def images(self):
        return [i.image for i in self.image_set.all()]

    def available(self):
        return self.reserved_for is None
    
    def __str__(self):
        if self.creation_year:
            return f'[{self.collection_id}] {self.creation_year} {self.title}'
        else:
            return f'[{self.collection_id}] {self.title}'

