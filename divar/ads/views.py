from django.http import HttpResponse , JsonResponse
from ads.models import *



def show_all_ads(request):
    ads = Ad.objects.all().values('title', 'category__title', 'description', 'price', 'city__name', 'created_at')

    return JsonResponse(list(ads), safe=False)


def ads_search_by_city(request, city):
    ads = Ad.objects.filter(city__name=city).values('id', 'title', 'price', 'category__title')

    return JsonResponse(list(ads), safe=False)


def ads_search_by_category(request, category):
    ads = Ad.objects.filter(category__title=category).values('id', 'category__title', 'city__name')

    return JsonResponse(list(ads), safe=False)