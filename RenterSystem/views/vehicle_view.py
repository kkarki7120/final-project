from django.shortcuts import redirect, render
from django.views import View
from UserManagementSystem.models.registerModel import CustomUser
from VendorSystem.models.vehicle_type import VehiclesTypes , Company_name
from VendorSystem.models.add_vehicle import AddVehicles
from ReserveSystem.models.reserve import Reserved_vehicle
from django.db.models import Count
from datetime import datetime


# Create your views here.


     
class Vehicle_view(View):
    def get(self,request):
        #extracting user object by id
        # id=request.session.get('id')
        # vehicle_type=VehiclesTypes.get_all_data()
        # vehicle= AddVehicles.get_all_data()

        pickupAddress = request.session.get('pickupAddress')
        pickupDate = request.session.get('pickupDate')
        pickupTime = request.session.get('pickupTime')
        dropoffDate = request.session.get('dropoffDate')
        seats = request.session.get('seats')
        print(seats)
      
        


        #to extract vendor vehicle given by user
        vendor = CustomUser.get_user_by_address(pickupAddress).values_list('id', flat=True)
        print(vendor)
        if vendor:
            print(vendor)
        else:
            print("no data")


        
        #checking date avaiability of vehicle
        pickup_datetime = (datetime.strptime(str(pickupDate),'%Y-%m-%d') )
        dropoff_datetime = (datetime.strptime(str(dropoffDate),'%Y-%m-%d'))   
        reserved_vehicles = Reserved_vehicle.objects.filter(pickup_date__lt=dropoff_datetime, dropoff_date__gt=pickup_datetime)
        reserved_vehicle_ids = reserved_vehicles.values_list('reserved_vehicle_id', flat=True)

        #extracting  vehicle from vehicle id
        vendor_vehicle = AddVehicles.get_all_vehicle_by_useridlist(vendor).exclude(id__in=reserved_vehicle_ids)
        similar_vehicle = vendor_vehicle.filter(no_of_seats__gt=seats)
        print(similar_vehicle)
        vendor_vehicle = vendor_vehicle.filter(no_of_seats=seats)
        vendor_vehicle = vendor_vehicle.filter(status='Active')
        

        vehicle_count={}

        if vendor_vehicle:
            vendor_vehicle_count = AddVehicles.get_all_vehicle_by_useridlist(vendor).count()
            vehicle_count = AddVehicles.get_all_vehicle_by_useridlist(vendor).count()
            
        else:
            vendor_vehicle_count=0
            vehicle_count=0
            print("no data")
    
       
                
     
        #applying filter
        #for vehicle type
        total_vehicle_count= AddVehicles.objects.all().count()
        vehicle_type= VehiclesTypes.objects.annotate(type = Count('addvehicles'))
        #fetching type id from url
        type_id= request.GET.get("category")
        print("category")
        print(type_id)

        if type_id:
            vendor_vehicle = AddVehicles.get_vehicle_by_vehicle_type(type_id)
            vendor_vehicle_count= AddVehicles.get_vehicle_by_vehicle_type(type_id).count()
            if len(vendor_vehicle)==0:
                vendor_vehicle = AddVehicles.get_all_vehicle_by_useridlist(vendor)
                vendor_vehicle_count=0
            
        #for brands type

        brands_type = Company_name.objects.annotate(type = Count('addvehicles'))
        #fetching brand id from url
        brand_id= request.GET.get("brand")
        print(brand_id)
        if brand_id:
            vendor_vehicle = AddVehicles.get_vehicle_by_vehicle_type(brand_id)
            vendor_vehicle_count= AddVehicles.get_vehicle_by_vehicle_type(brand_id).count()
            if len(vendor_vehicle)==0:
                vendor_vehicle = AddVehicles.get_all_vehicle_by_useridlist(vendor)
                vendor_vehicle_count=0
        
        #for price
        LowTOHigh = request.GET.get("Price_LOWTOHIGH")

        if LowTOHigh:
            vendor_vehicle = AddVehicles.get_all_vehicle_by_useridlist(vendor).order_by('price')

        HighTOLow = request.GET.get("Price_HIGHTOLOW")

        if HighTOLow:
            vendor_vehicle = AddVehicles.get_all_vehicle_by_useridlist(vendor).order_by('-price')
        
     

        

        dict={
            'pickupAddress': pickupAddress,
            'pckupDate': pickupDate,
            'pickupTime':pickupTime,
            'dropoffDate':dropoffDate,
            'vehicle':vendor_vehicle,
            'vehicle_type':vehicle_type,
            'vehicle_count':vehicle_count,
            'vehicle_type_count':vendor_vehicle_count,
            'total_vehicle_count':total_vehicle_count,
            'similar_vehicle':similar_vehicle,
            #for brand
            'brands_type':brands_type
        }

     

    
        return render(request , 'user/vehicle_view.html',dict)
       
    def post(self,request):
        postData = request.POST
        vehicle_id = postData.get('Vehicle_id')
        #vehicle object 
        reserved_vehicle=AddVehicles.get_vehicle_by_id(vehicle_id)

        user = request.session.get('user')
        #renter object
        renter = CustomUser.get_user_by_email(user)

        #Reserved_vehicle object
        vehicle_reservation=Reserved_vehicle(renter_user = renter, reserved_vehicle=reserved_vehicle )

        vehicle_reservation.save()

        return redirect('Reserved_vehicle')


        
