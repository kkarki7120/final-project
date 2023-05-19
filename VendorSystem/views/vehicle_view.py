from django.shortcuts import redirect, render
from VendorSystem.models.add_vehicle import AddVehicles




# Create your views here.


     
def vehicle_view(request):
    #extracting user object by id
    id=request.session.get('id')

   
    

    vehicle=AddVehicles.get_all_vehicle_by_userid(id)
    print(id)
    print('-------------')
    print(vehicle)



    data={
        'vehicle':vehicle
    }

    return render(request , 'dashboard/view_vehicle.html',data)


def delete_vehicle(request,slug):
    vehicle= AddVehicles.objects.get(slug=slug)
    vehicle.delete_vehicle()

    return redirect('view_vehicles')










    