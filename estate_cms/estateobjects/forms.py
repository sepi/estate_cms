from django import forms

class BidForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            #visible.field.widget.attrs['placeholder'] = visible.field.label

    name = forms.CharField(
        label="Full Name",
        help_text="Your full name (required)"
    )
    email_address = forms.EmailField(
        label="Email address",
        help_text="Your valid email-address (required)"
    )
    post_address = forms.CharField(
        label="Post address",
        required=False,
        help_text="Your postal address (optional)",
        widget=forms.Textarea
    )
    phone_number = forms.CharField(
        label="Phone number",
        required=False,
        help_text="A valid phone number including prefix (eg. +352, optional)"
    )

    price = forms.IntegerField(
        label="Price",
        initial=0,
        help_text="An indication of the price you are willing to pay. We might gift you the objet if you put in 0."
    )
