from django.shortcuts import redirect, render
from django.views import View
from VendorSystem.models.vehicle_type import VehiclesTypes
from VendorSystem.models.add_vehicle import AddVehicles
from UserManagementSystem.models.add_location import Add_location
from django.contrib import messages
from datetime import datetime
from datetime import date



# Create your views here.


     
class Landing_page(View):
    def get(self,request):
        #extracting user object by id
        id=request.session.get('id')
        user_type= request.session.get('user_type')
        if not user_type:
            district=Add_location.get_all_data()
            dict={
                "dic":district
            }
            vehicle_type=VehiclesTypes.get_all_data()
            vehicle= AddVehicles.get_all_data()

            dict={
                'type': vehicle_type,
                'vehicle': vehicle,
                'dic':district
            }
            return render(request , 'index.html',dict)
        else:
            return redirect('userIndex')
        
        
        


    def post(self,request):
        # saving  data in variable
        postData = request.POST
        pickupAddress= postData.get('pickup')
        pickupDate=postData.get('pickupdate')
        pickupTime=postData.get('pickuptime')
        dropoffDate=postData.get('dropoffdate')
        seats = postData.get('seats')
        
        
        
        print(pickupDate)
        print(dropoffDate)

        no_of_days=datetime.strptime(str(dropoffDate),'%Y-%m-%d')-datetime.strptime(str(pickupDate),'%Y-%m-%d')
        
        print(no_of_days.days)

        today_date=date.today()
        print(today_date)

        error_msg=""

        if(datetime.strptime(str(pickupDate),'%Y-%m-%d') < datetime.strptime(str(today_date),'%Y-%m-%d')):
            error_msg="pickup date cannot be past date"
        elif(datetime.strptime(str(pickupDate),'%Y-%m-%d') == datetime.strptime(str(today_date),'%Y-%m-%d')):
            error_msg="Dropoff date should be more than present date"
        elif(datetime.strptime(str(dropoffDate),'%Y-%m-%d') == datetime.strptime(str(today_date),'%Y-%m-%d')):
            error_msg="Dropoff date should be more than present date"
        elif(datetime.strptime(str(dropoffDate),'%Y-%m-%d') < datetime.strptime(str(today_date),'%Y-%m-%d')):
            error_msg="dropoff date cannot be past date"
        elif(datetime.strptime(str(dropoffDate),'%Y-%m-%d') == datetime.strptime(str(pickupDate),'%Y-%m-%d')):
            error_msg="pickup date and dropoff date cannot be same date"
        elif(datetime.strptime(str(dropoffDate),'%Y-%m-%d') < datetime.strptime(str(pickupDate),'%Y-%m-%d')):
            error_msg="Dropoff date cannot be past date than pickup date"
        
    


    
        if error_msg:
            messages.error(request,f"{error_msg}")
            return redirect('userIndex')
        else:
            request.session['pickupAddress']=pickupAddress
            request.session['pickupDate']=pickupDate
            request.session['pickupTime']=pickupTime
            request.session['dropoffDate']=dropoffDate
            request.session['seats']=seats
            

            return redirect(  'viewallvehicle')


        def date_validation(pickupDate,dropoffDate):
            pass
