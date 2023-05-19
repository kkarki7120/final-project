from django.contrib import admin
from ReserveSystem.models.reserve import Reserved_vehicle


# Register your models here.



class Reserved_vehicleAdmin(admin.ModelAdmin):
    list_display=['renter_user','reserved_vehicle','pickup_date','Payment_Choices','Payment_done','reserve_choice']
    list_filter =['pickup_date','Payment_Choices','Payment_done','reserve_choice']

admin.site.register(Reserved_vehicle,Reserved_vehicleAdmin)