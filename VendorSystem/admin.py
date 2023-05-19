from django.contrib import admin
from .models.vehicle_type import VehiclesTypes , Company_name
from .models.vehicle_type import Fuel_type
from .models.add_vehicle import AddVehicles
from .models.vendor_feedback import VendorFeedback

class CompanyNameAdmin(admin.ModelAdmin):
    search_fields=('name',)
    list_display=['name','status']

# Register your models here.
admin.site.register(VehiclesTypes)
admin.site.register(Fuel_type)
admin.site.register(AddVehicles)
admin.site.register(VendorFeedback)
admin.site.register(Company_name,CompanyNameAdmin)
