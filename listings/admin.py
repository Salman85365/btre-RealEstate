from django.contrib import admin
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id','price','is_published','list_date','realtor')
    list_display_links=('id','realtor','price')
    list_editable=('is_published',)
    list_filter=('realtor',)
    search_fields = ('id','price','zipcode','state','city','realtor')

admin.site.register(Listing, ListingAdmin)