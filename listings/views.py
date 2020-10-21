from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .models import Listing
from .choices import price_choices,bedroom_choices,state_choices

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
    listing = get_object_or_404(Listing,pk=listing_id)
    context = {
        'listing': listing
    }

    return render(request,'listing/listing.html',context)
 

def search(request):
    queryset_list= Listing.objects.order_by('-list_date')

    #keywords
    if 'keywords' in request.GET:
        keywords= request.GET['keywords']
        if keywords:
            queryset_list=queryset_list.filter(description__icontains=keywords)

    # city
    if 'city' in request.GET:
        citys = request.GET['city']
        if citys:
             queryset_list = queryset_list.filter(city__iexact=citys)

    # state
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
             queryset_list = queryset_list.filter(city__iexact=state)

    # bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

    # price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    context = {
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'listings': queryset_list
    }
    return render(request,'listing/search.html',context)
