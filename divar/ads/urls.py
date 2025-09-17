from django.urls import path
from ads.views import *


urlpatterns = [
    path('all-list/', show_all_ads),
    path('city/<str:city>/', ads_search_by_city),
    path('category/<str:category>/', ads_search_by_category, name='ads_search_by_category'),
    path('delete/<int:ad_id>/' , delete_ad, name='delete_ad'),
]