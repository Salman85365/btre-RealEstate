from django.contrib import admin
from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    list_display =('name','hire_date','email','phone')
    list_display_links=('name','email','phone')
    search_fields=('name','email')


admin.site.register(Realtor, RealtorAdmin)
# Register your models here.
