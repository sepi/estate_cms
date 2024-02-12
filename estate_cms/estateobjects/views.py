from django.views.generic import DetailView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.contrib import messages
from django.core.exceptions import PermissionDenied

from .models import EstateObject, Bid, Contact
from .forms import BidForm

def find_contact_by_match(cd):
    contact = Contact.objects.get(name=cd['name'],
                                  email_address=cd['email_address'],
                                  post_address=cd['post_address'],
                                  phone_number=cd['phone_number'])
    return contact

class EstateObjectDetailView(DetailView):
    model = EstateObject

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Find a previous bid on this object based on session bidder
        session_bidder = self.request.session.get('bidder')
        if session_bidder:
            try:
                bidder = find_contact_by_match(session_bidder)
                try:
                    bid = Bid.objects.get(bidder=bidder,
                                          estate_object=kwargs['object'])
                    context["already_bid"] = True
                except Bid.DoesNotExist:
                    pass
            except Contact.DoesNotExist:
                pass
            
            # Pre-fill form for bid on new object
            context["bid_form"] = BidForm(initial=session_bidder)
        else:
            context["bid_form"] = BidForm()
            context["already_bid"] = False
        
        return context

def place_bid(request, pk):
    form = BidForm(request.POST)

    if form.is_valid():
        eo = get_object_or_404(EstateObject, pk=pk)

        if not eo.available():
            raise PermissionDenied()
            
        cd = form.cleaned_data

        # Find bidder with exact values in database
        try:
            bidder = find_contact_by_match(cd)
        except Contact.DoesNotExist:
            bidder = Contact(name=cd['name'],
                             email_address=cd['email_address'],
                             post_address=cd['post_address'],
                             phone_number=cd['phone_number'])
        bidder.save()
        
        bid = Bid(estate_object=eo,
                  price=cd['price'],
                  bidder=bidder)
        bid.save()

        from django.core.serializers import serialize

        request.session['bidder'] = {
            'name': bidder.name,
            'email_address': bidder.email_address,
            'post_address': bidder.post_address,
            'phone_number': bidder.phone_number
        }

        messages.add_message(request, messages.INFO, "Successfully created bid.")
        return HttpResponseRedirect(reverse('estateobjects:detail', kwargs={'pk': pk}))
    else:
        print("Invalid")
        messages.add_message(request, messages.ERROR, "Could not create bid.")
        return HttpResponseRedirect(reverse('estateobjects:detail', kwargs={'pk': pk}))
