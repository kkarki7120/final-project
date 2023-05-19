from django.shortcuts import redirect, render
from django.views import View
from UserManagementSystem.models.registerModel import CustomUser , Add_location
from ReserveSystem.models.reserve import Reserved_vehicle
from VendorSystem.models.vehicle_type import VehiclesTypes , Company_name
from VendorSystem.models.add_vehicle import AddVehicles
from datetime import datetime
from django.contrib import messages


# Create your views here.


     
class Vehicle_details(View):
    def get(self,request,slug):
        

        pickupAddress = request.session.get('pickupAddress')
        pickupDate = request.session.get('pickupDate')
        pickupTime = request.session.get('pickupTime')
        dropoffDate = request.session.get('dropoffDate')
        
        print("-----------")
        print(pickupAddress)
        print(pickupDate)
        print(pickupTime)
        print(dropoffDate)
        print("-----------")

        no_of_days=datetime.strptime(str(dropoffDate),'%Y-%m-%d')-datetime.strptime(str(pickupDate),'%Y-%m-%d')
       
        vehicle=AddVehicles.objects.get(slug=slug)
        print(vehicle.id)

        pickupAddress= Add_location.objects.get(id=pickupAddress)

        price = vehicle.price
        total = vehicle.price*no_of_days.days
        


        dict={
            'pickupAddress': pickupAddress,
            'pckupDate': pickupDate,
            'pickupTime':pickupTime,
            'dropoffDate':dropoffDate,
            'vec': vehicle,
            'days':no_of_days.days,
            'price': price,
            'total':total,
            'id' : slug
            

        }


        return render(request , 'user/vehicle_detail.html', dict)

    def post(self,request,slug):
       
        pickupAddress = request.session.get('pickupAddress')
        pickupDate = request.session.get('pickupDate')
        pickupTime = request.session.get('pickupTime')
        dropoffDate = request.session.get('dropoffDate')
        user = request.session.get('user')
        
        no_of_days=datetime.strptime(str(dropoffDate),'%Y-%m-%d')-datetime.strptime(str(pickupDate),'%Y-%m-%d')
       
        vehicle=AddVehicles.objects.get(slug=slug)
        
        print(vehicle)
        print(slug)
        
        # status = vehicle.status
        # vehicle.status = "Inactive"
        # vehicle.save()
        vec_id = vehicle.id
        price = vehicle.price
        total = vehicle.price*no_of_days.days
        print(total)

        #reserved vehicle id object
        reserved_vehicle=AddVehicles.get_vehicle_by_id(vec_id)
            #user object
        renter = CustomUser.get_user_by_email(user)
            
        vehicle_reservations = Reserved_vehicle(renter_user=renter , reserved_vehicle = reserved_vehicle, pickup_address= pickupAddress , pickup_date=pickupDate, dropoff_date=dropoffDate,pickup_time=pickupTime , Payment_Choices = "pay_on_cash", Payment_amount = price)
        vehicle_reservations.save()

             
    
        
        
        dict = {
            'pickupAddress': pickupAddress,
            'pckupDate': pickupDate,
            'pickupTime':pickupTime,
            'dropoffDate':dropoffDate,
            'vec': vehicle,
            'days':no_of_days.days,
            'price': price,
            'total':total,
            'id':slug,
            
        }

        messages.success(request,'Your vehicle has been reserved successfully, please check your reservation list. ')
        return render(request , 'user/vehicle_detail.html',dict)

        
# def finish_vehicle(request, slug):
#     # Retrieve the vehicle by its ID
#     vehicle = AddVehicles.objects.get(slug=slug)

#     # Update the status of the vehicle to 'active'
#     vehicle.status = 'active'
#     vehicle.save()

#     # Other logic for finishing the service
#     # ...

#     # Redirect to a success page or render a success template
#     return render(request , 'user/vehicle_detail.html')
