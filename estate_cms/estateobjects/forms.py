from django import forms
from django.utils.translation import gettext_lazy as _

class BidForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            #visible.field.widget.attrs['placeholder'] = visible.field.label

    name = forms.CharField(
        label=_("Full Name *"),
        help_text=_("Your first and second name")
    )
    email_address = forms.EmailField(
        label=_("Email address *"),
        help_text=_("Your email-address")
    )
    post_address = forms.CharField(
        label=_("Post address"),
        required=False,
        help_text=_("Your postal address (optional)"),
        widget=forms.Textarea
    )
    phone_number = forms.CharField(
        label=_("Phone number"),
        required=False,
        help_text=_("A phone number including prefix (eg. +352, optional)")
    )

    price = forms.IntegerField(
        label=_("Price you want to pay in € *"),
        initial=0,
        help_text=_("An indication of the price you are willing to pay. We might gift you the objet if you put in 0.")
    )
