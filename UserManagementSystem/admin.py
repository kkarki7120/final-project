from django.contrib import admin
from .models.add_location import Add_location
from .models.registerModel import CustomUser
from .models.contact_us import Contact_Us

# Register your models here.


class CustomUserAdmin(admin.ModelAdmin):
    search_fields=('username',)
    list_display=['username','email','created_at','user_type','status']
    list_filter =['user_type','created_at']

class ContactusAdmin(admin.ModelAdmin):
    search_fields=('full_name',)
    list_display=['full_name','email','date','message']
    list_filter =['date']

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Contact_Us,ContactusAdmin)
admin.site.register(Add_location)
