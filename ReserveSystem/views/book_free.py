# from django.views import View
# import requests
# from VendorSystem.models.add_vehicle import AddVehicles
# from ReserveSystem.models.reserve import Reserved_vehicle
# from UserManagementSystem.models.registerModel import CustomUser






# class BookFree(View):
            
#     def get(self,request): 

#         pickupAddress = request.session.get('pickupAddress')
#         pickupDate = request.session.get('pickupDate')
#         pickupTime = request.session.get('pickupTime')
#         dropoffDate = request.session.get('dropoffDate')
#         user = request.session.get('user')
#         vec_id = request.GET.get("vec_id")
               
#         #reserved vehicle id object
#         reserved_vehicle=AddVehicles.get_vehicle_by_id(vec_id)
#         #user object
#         renter = CustomUser.get_user_by_email(user)
            
#         vehicle_reservations = Reserved_vehicle(renter_user=renter , reserved_vehicle = reserved_vehicle, pickup_address= pickupAddress , pickup_date=pickupDate, dropoff_date=dropoffDate,pickup_time=pickupTime , Payment_Choices = "Khalti", Payment_amount=amount ,Payment_done=True)
#         vehicle_reservations.save()



#     def post(self):
#               pass