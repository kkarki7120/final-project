from django.urls import path
from .views import login,home
from .views  import register, register_as_vendor, register_as_customer, editProfile
from ReserveSystem.views.reserve_request import  VendorReservedVehicle, del_reserved_request
from RenterSystem.views.vehicle_view import Vehicle_view
from VendorSystem.views import addvehicle , feedback , vehicle_view , edit_vehicle 
from RenterSystem.views.vehicle_details import Vehicle_details
from ReserveSystem.views.reserved_vehicle import ReservedVehicle, del_reserved_vehicle
from RenterSystem.views.user_landing import Landing_page
from .views.contact import Contact_US
from .middlewares.auth import auth_middleware as login_required
from django.contrib import admin
from ReserveSystem.views.khalti import KhaltiVerify


urlpatterns = [
    path('', Landing_page.as_view() , name="index"),
    path('user/', login_required(home.userIndex), name = "userIndex" ),
    path('register_as_vendor/', register_as_vendor.RegisterVendor.as_view(), name = "register_as_vendor" ),
    path('login/', login.Login.as_view(), name = "login"),
    path('register/', register.register, name = "register" ),
    path('register_as_customer/', register_as_customer.RegisterCustomer.as_view(), name = "register_as_customer" ),
    path('contact/', Contact_US.as_view() , name="contact"),
    path('logout/', login_required(login.logout), name = "logout" ),
    path('editProfile/',editProfile.EditProfile.as_view() , name="editProfile"),
    # vendor
    path('vendor/addVehicles/', addvehicle.AddVehicle.as_view() , name="add_vehicles"),
    path('vendor/viewVehicles/',login_required( vehicle_view.vehicle_view) , name="view_vehicles"),
    path('vendor/viewVehicles/edit/<slug:slug>',edit_vehicle.EditVehicle.as_view() , name="edit_vehicles"),
    path('vendor/viewVehicles/delete/<slug:slug>',vehicle_view.delete_vehicle , name="delete_vehicles"), 
    path('vendor/feedback',feedback.Feedback.as_view(), name="feedback"),
    # vendor reserved vehicle
    path('user/Request_Reserved_vehicle/',VendorReservedVehicle.as_view() , name="reserve_request"),
    path('user/Request_Reserved_vehicle/delete/<str:id>', del_reserved_request , name="delete_reserved_request"),
    path('vehicle/<slug:slug>',Vehicle_details.as_view(),name="vehicledetail" ),
    path('vehicle/',Vehicle_view.as_view(),name="viewallvehicle" ),
    
    # user reserved vehicle
    path('user/Reserved_vehicle/',login_required( ReservedVehicle.as_view()) , name="Reserved_vehicle"),
    path('user/Reserved_vehicle/delete/<str:id>', del_reserved_vehicle , name="delete_reserved_vehicles"), 
    
    #khalti view
    path('vehicle/khalti-verify/', KhaltiVerify.as_view() , name="khaltiverify"),

]