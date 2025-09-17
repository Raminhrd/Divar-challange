from django.http import HttpResponse , JsonResponse
from ads.models import *



def show_all_ads(request):
    ads = Ad.objects.all().values('title', 'category__title', 'description', 'price', 'city__name', 'created_at')

    return JsonResponse(list(ads), safe=False)


def ads_search_by_city(request, city):
    ads = Ad.objects.filter(city__name__iexact=city).values('id', 'title', 'price', 'category__title')

    return JsonResponse(list(ads), safe=False)


def ads_search_by_category(request, category):
    ads = Ad.objects.filter(category__title__iexact=category).values('id', 'title', 'price', 'category__title', 'city__name')

    return JsonResponse(list(ads), safe=False)

def delete_ad(request, ad_id):
    try:
        ad = Ad.objects.get(id=ad_id)
        ad.delete()
        return JsonResponse({"status": "success", "message": "Ad deleted"})
    
    except Ad.DoesNotExist:
        return JsonResponse({"status": "error", "message": "Ad not found"})
    