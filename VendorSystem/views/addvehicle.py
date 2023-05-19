from django.shortcuts import redirect, render
from VendorSystem.models import vehicle_type
from VendorSystem.models.add_vehicle import AddVehicles
from VendorSystem.models.vehicle_type import VehiclesTypes , Fuel_type,Company_name
from UserManagementSystem.models.registerModel import CustomUser
from django.views import View
from django.contrib import messages




# Create your views here.


     
class AddVehicle(View):
    def get(self, request):
        #fetching data from database
        vehicleType = vehicle_type.VehiclesTypes.get_all_data
        fuelType = vehicle_type.Fuel_type.get_all_data
        company_name= vehicle_type.Company_name.get_all_data
        #sending fetch data to html through dictionary
        dict={
            'vehicle_type':vehicleType,
            'fuel_type'  : fuelType,
            'company_name':company_name
        }
        return render(request , 'dashboard/add_vehicle.html',dict)
    def post(self, request):
        # saving user send data in variable
        postData = request.POST
        vehicle_picture=request.FILES.get('picture')
        vehicle_number =postData.get('vehicle_number')
        model_name =postData.get('model_name')
        company_name_id =postData.get('company_name')
        vehicletype_id =postData.get('vehicletype')
        fuel_type_id =postData.get('fuel_type')
        price =postData.get('price')
        color  =postData.get('color')
        seats =postData.get('seats')
        geartype=postData.get('geartype')
        status  =postData.get('status')


        
        #extracting vehicletype object by id
        vehicletype = VehiclesTypes.get_all_data_by_id(vehicletype_id)

        #extracting fueltype object by id
        fuel_type = Fuel_type.get_all_data_by_id(fuel_type_id)

        #extracting fueltype object by id
        company_name = Company_name.get_all_data_by_id(company_name_id)

        #extracting user object by id
        id=request.session.get('id')
        user = CustomUser.get_user_by_id(id)


        # fuel_type=Fuel_type.id
        # vehicletype=vehicletype.VehiclesTypes

        #creatind assvehicles object
        vehicle = AddVehicles(user=user,picture = vehicle_picture , company_name = company_name , model = model_name , color = color , price = price ,  no_of_seats = seats,  fuel_type = fuel_type , vehicle_type = vehicletype, gear = geartype , status = status, vehicle_number = vehicle_number )

        #saving user entered value in dictionary
        entered_value ={'vehicle_picture':vehicle_picture , 'company_name':company_name, 'model_name': model_name , 'color':color , 'price' : price ,  'seats' : seats,  'fuel_type': fuel_type , 'vehicletype' : vehicletype,'geartype' : geartype , 'status' : status, vehicle_number : 'vehicle_number'}

        #checking validation from backend
        error_msg= None

        
        if vehicle.isExists_vehicle_number():
            error_msg="Vehicle number already exists"
        elif (not model_name):
            error_msg="please enter vehicle model name"
        elif (not company_name):
            error_msg="please enter vehicle company name"
        elif (not vehicle_number):
            error_msg="please enter vehicle Number"
        elif (not price):
            error_msg="please enter your username"





        data={
            'values':entered_value,
            'error':error_msg
        }
        if not error_msg:
            vehicle.addVehicle()
            messages.success(request,'Vehicle is sucessfully added')
            return redirect('add_vehicles')
    
        return render(request , 'dashboard/add_vehicle.html',data)

    

