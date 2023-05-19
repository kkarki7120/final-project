from django.db import models
from UserManagementSystem.models.registerModel import CustomUser
from VendorSystem.models.add_vehicle import AddVehicles


# user models
class Reserved_vehicle(models.Model):
    Status = (('Active','Active'),('Inactive','Inactive'))
    Reservation_Choices = (('Accepted','Accepted'),('Rejected','Rejected'))
    Payment_Choices = (('Khalti','Khalti'),("pay_on_cash","pay_on_cash"))

    id = models.AutoField(primary_key=True,  unique=True)
    renter_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    reserved_vehicle=models.ForeignKey(AddVehicles, on_delete=models.CASCADE)

    reserve_choice= models.CharField(choices=Reservation_Choices, max_length=25, default='Pending')
    pickup_address= models.CharField(max_length=50 ,default=False, null=True,blank=True)
    pickup_date = models.DateField(default=None)
    dropoff_date= models.DateField(default=None)
    pickup_time = models.TimeField(default=None)
    Payment_Choices = models.CharField(choices=Payment_Choices, max_length=50,default=None)
    
    Payment_amount = models.CharField(max_length=25 , default=None )
    reserved_date = models.DateTimeField(auto_now=True)

    Payment_done = models.BooleanField(default=False,null=True,blank=True)
    status= models.CharField(choices= Status, max_length=25, default='Active')
    completed = models.BooleanField(default=False)
    completed_date = models.DateTimeField(null=True, blank=True)

    def get_reservation_by_id(id):
        try:
            return Reserved_vehicle.objects.filter(id = id)
        except:
            return False
  

    @staticmethod
    def get_reserved_vehicle_by_userid(id):
        try:
            return Reserved_vehicle.objects.filter(renter_user = id)
        except:
            return False
  

