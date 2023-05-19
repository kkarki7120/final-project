from django.shortcuts import redirect, render
from django.views import View
from ReserveSystem.models.reserve import Reserved_vehicle
from UserManagementSystem.models.registerModel import CustomUser
from VendorSystem.models.add_vehicle import AddVehicles




# Create your views here.


     
class ReservedVehicle(View):
    def get(self,request):
        user_id=request.session.get('id')

        reserved_vehicle = Reserved_vehicle.get_reserved_vehicle_by_userid(user_id)

      

        dict={
            'res_vehicle':reserved_vehicle,
            
        }
    
        return render(request , 'user/reservation.html',dict)

    def post(self,request):
        pass



def del_reserved_vehicle(request,id):
    vehicle= Reserved_vehicle.get_reservation_by_id(id)
    vehicle.delete()

    return redirect('Reserved_vehicle')