from django.shortcuts import render
from listings.models import Listing
from listings.choices import price_choices,type_choices
def index(request):
    listings = Listing.objects.all()[:3]
    context = {
        'listings':listings,
        'price_choices':price_choices,
        'type_choices':type_choices
    }
    return render(request,'pages/index.html',context)
def about(request):
    return render(request,'pages/about.html')