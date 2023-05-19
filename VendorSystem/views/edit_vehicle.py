from django.shortcuts import redirect, render
from VendorSystem.models import vehicle_type
from VendorSystem.models.add_vehicle import AddVehicles,Company_name
from VendorSystem.models.vehicle_type import VehiclesTypes , Fuel_type
from django.views import View
from django.contrib import messages




# Create your views here.


     
class EditVehicle(View):
    def get(self, request,slug):
        #fetching data from database
        vehicleType = vehicle_type.VehiclesTypes.get_all_data
        fuelType = vehicle_type.Fuel_type.get_all_data
        company_name= vehicle_type.Company_name.get_all_data
        vehicle=AddVehicles.objects.get(slug=slug)
      
        dict={ 
         'values':vehicle,
         'vehicle_type':vehicleType,
         'fuel_type'  : fuelType,
         'company_name': company_name,
         'id':slug
        }
     
        return render(request , 'dashboard/edit_vehicle.html', dict)

    def post(self, request ,slug):
        # saving user send data in variable
        postData = request.POST

        vehicle_picture=request.FILES.get('picture')
        model_name =postData.get('model_name')
        company_name_id =postData.get('company_name')
        vehicletype_id =postData.get('vehicletype')
        fuel_type_id =postData.get('fuel_type')
        price =postData.get('price')
        discounted_price=postData.get('discounted_price')
        color  =postData.get('color')
        seats =postData.get('seats')
        geartype=postData.get('geartype')
        status  =postData.get('status')

        print(slug)

         
        #extracting vehicletype object by id
        vehicletype = VehiclesTypes.get_all_data_by_id(vehicletype_id)

        #extracting fueltype object by id
        fuel_type = Fuel_type.get_all_data_by_id(fuel_type_id)

        company_name = Company_name.get_all_data_by_id(company_name_id)

        #vehicle object
        vec=AddVehicles.objects.get(slug=slug)
        error_msg=None

        #changing data
        if vehicle_picture != None and vehicle_picture != " " :
            vec.picture=vehicle_picture
        vec.company_name=company_name
        vec.model=model_name
        vec.color=color
        vec.price=price
        vec.discounted_price=discounted_price
        vec.no_of_seats=seats
        vec.fuel_type=fuel_type
        vec.vehicle_type=vehicletype
        vec.geartype=geartype
        vec.status=status

        vec.update_vehicle()


        dict={
         'values':vec,
         'vehicle_type':vehicletype,
         'fuel_type'  : fuel_type

        }

        messages.success(request,'your vehicle is updated')
     
        return redirect('/vendor/viewVehicles/edit/'+f'{slug}',dict)



