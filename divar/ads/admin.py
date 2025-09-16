from django.contrib import admin
from ads.models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title' , 'description']
    search_fields = ['title']


class CityAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


class AdsAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'description', 'price', 'city', 'created_at']
    search_fields = ['title']
    list_filter = ['city', 'category']



admin.site.register(Category, CategoryAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Ad, AdsAdmin)