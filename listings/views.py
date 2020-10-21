from django.shortcuts import render

from .models import Listing
# Create your views here.
def listings(request):
    listings=Listing.objects.all()

    context={
        'listings': listings
    }
    return render(request,'listing/listings.html',context)
 
def listing(request,listing_id):
    return render(request,'listing/listing.html')
 

def search(request):
    return render(request,'listing/search.html')
 