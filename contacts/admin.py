from django.contrib import admin
from .models import contact
class ContactAdmin(admin.ModelAdmin):
    list_display=('user_id','email','phone','name','listing')
    list_display_links =('user_id','email')
    list_per_page=25

admin.site.register(contact,ContactAdmin)

