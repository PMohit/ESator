from django.shortcuts import render
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .models import Listing


def listings(request):
    listings=Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings,3)
    page=request.GET.get('page')
    paged_listings=paginator.get_page(page)

    context={
        'listings': paged_listings
    }
    return render(request,'listing/listings.html',context)
 
def listing(request,listing_id):
    return render(request,'listing/listing.html')
 

def search(request):
    return render(request,'listing/search.html')
