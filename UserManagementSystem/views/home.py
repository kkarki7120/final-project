from itertools import count
from django.shortcuts import redirect, render
from UserManagementSystem.models.registerModel import CustomUser
from VendorSystem.models.vehicle_type import VehiclesTypes
from VendorSystem.models.add_vehicle import AddVehicles
from UserManagementSystem.models.add_location import Add_location
from VendorSystem.models.vendor_feedback import VendorFeedback
from ReserveSystem.models.reserve import Reserved_vehicle


     
def userIndex(request):
    user_type= request.session.get('user_type')
    if user_type != "Vendor":
        location=Add_location.get_all_data()
        loc={
            "loc":location
        }
        vehicle_type=VehiclesTypes.get_all_data()
        vehicle= AddVehicles.get_all_data()

        dict={
            'type': vehicle_type,
            'vehicle': vehicle,
            'loc':location
        }
        return render(request , 'index.html',dict)
    else:
        id=request.session.get('id')
        Renter_count = CustomUser.objects.filter(user_type='Renter').count
        vehicle_count=AddVehicles.get_all_vehicle_by_userid(id).count
        feedback_count = VendorFeedback.get_all_feedback_by_userid(id).count
        vehicle = Reserved_vehicle.objects.all()
        count=0

        for i in vehicle:
            if id == i.reserved_vehicle.user.id:
                count+=1

        reserved_count=count

        dict={
            'renter_count' : Renter_count,
            'vehicle_count' : vehicle_count,
            'feedback_count' : feedback_count,
            'reserved_count':reserved_count,
            
        }
        return render(request , 'dashboard/dash.html' , dict )





