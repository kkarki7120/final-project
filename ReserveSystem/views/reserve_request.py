from django.shortcuts import redirect, render
from django.views import View
from ReserveSystem.models.reserve import Reserved_vehicle
from VendorSystem.models.add_vehicle import AddVehicles
from datetime import datetime
from UserManagementSystem.models.registerModel import CustomUser , Add_location
from datetime import datetime





# Create your views here.


     
class VendorReservedVehicle(View):
    def get(self,request):
        user_id=request.session.get('id')
        print(user_id)

        
        res_vehicle = Reserved_vehicle.objects.all()
        
        

        
        
       
       
        
        

        
        



        

     

      

        dict={
            'res_vehicle':res_vehicle,
            'user_id':user_id,
            
            
            
            
        }
        print(user_id)
    
        return render(request , 'dashboard/reserve_request.html',dict)

    def post(self,request):
        
        postData = request.POST
        reservation_id =postData.get('reservation_id')
        reservation_status_accepted =postData.get('reservation_status_accepted')
        reservation_status_rejected =postData.get('reservation_status_rejected')
        

        reservation_vehicle = Reserved_vehicle.objects.get(id=reservation_id)
       
        status = reservation_vehicle.status
        print(status)
       
        if reservation_status_accepted:
           reservation_vehicle.reserve_choice = "Accepted"
        else:
            reservation_vehicle.reserve_choice = "Rejected"
        
        
        dropoffDate = reservation_vehicle.dropoff_date
        dropoff_datetime = (datetime.strptime(str(dropoffDate),'%Y-%m-%d'))  
        current_datetime = datetime.now()
        if reservation_vehicle.completed or dropoff_datetime < current_datetime:
            reservation_vehicle.completed = True
            reservation_vehicle.completed_date = dropoff_datetime
        else:
             reservation_vehicle.completed = False
      

        reservation_vehicle.save()

       
        return redirect('reserve_request')


def del_reserved_request(request,id):
    vehicle= Reserved_vehicle.get_reservation_by_id(id)
    vehicle.delete()

    return redirect('reserve_request')