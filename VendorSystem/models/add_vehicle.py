from django.db import models
from UserManagementSystem.models.registerModel import CustomUser
from VendorSystem.models.vehicle_type import VehiclesTypes
from VendorSystem.models.vehicle_type import Fuel_type , Company_name
from django.utils.text import slugify

# # Create your models here.

# AddVehicles models
class AddVehicles(models.Model):
    Status = (('Active','Active'),('Inactive','Inactive'))
    Gear = (('Manual','Manual'),('Auto','Auto'))
    id = models.AutoField(primary_key=True,  unique=True)
    vehicle_number = models.CharField(default=None, unique=True, max_length=50)
    picture= models.ImageField(upload_to='media/vehicles',default='media/vehicles/default.jpg')
    company_name =  models.ForeignKey(Company_name, on_delete=models.CASCADE)
    model = models.CharField(max_length=150, default=None)
    color= models.CharField(max_length=50 , default=None)
    price = models.IntegerField(default=0)
    no_of_seats=models.IntegerField()
    fuel_type=models.ForeignKey(Fuel_type, on_delete=models.CASCADE,default=None)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    vehicle_type = models.ForeignKey(VehiclesTypes, on_delete=models.CASCADE)
    gear=models.CharField(choices= Gear, max_length=25, default='Manual')
    slug=models.SlugField(unique=True, default=None, null=False)
    status= models.CharField(choices= Status, max_length=25, default='Active')
    
    # to generate slug 
    def _generate_unique_slug(self):
        unique_slug = slugify(self.model)
        num = 1
        while AddVehicles.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(unique_slug, num)
            num += 1
        return unique_slug
    # To save in model in database
    def addVehicle(self):
        if not self.slug:
            self.slug = self._generate_unique_slug()
        self.save()
    # To update in model in database
    def update_vehicle(self):
        self.save()
    
     # To delete in model in database
    def delete_vehicle(self):
        self.delete()
            #returning data from database
    @staticmethod
    def get_all_data():
        try:
            return AddVehicles.objects.all()
        except:
            return False

    
    #check whether user with same vehicle number exist or not in database
    def isExists_vehicle_number(self):
        if AddVehicles.objects.filter(vehicle_number = self.vehicle_number):
            return True
        return False 


    # returning data from database by id
    @staticmethod
    def get_vehicle_by_id(id):
        try:
            return AddVehicles.objects.get(id = id)
        except:
            return False
        
   

    # returning data from database by vehicle_type
    @staticmethod
    def get_vehicle_by_vehicle_type(vehicle_type):
        try:
            return AddVehicles.objects.filter(vehicle_type = vehicle_type)
        except:
            return False

    # returning data from database by  id
    @staticmethod
    def get_all_vehicle_by_id(id):
        try:
            return AddVehicles.objects.filter(id__id__in = id.all())
        except:
            return False


    # returning data from database by user id
    @staticmethod
    def get_all_vehicle_by_userid(id):
        try:
            return AddVehicles.objects.filter(user__id= id)
        except:
            return False
    @staticmethod
    def get_all_vehicle_by_useridlist(id):
        try:
            return AddVehicles.objects.filter(user__id__in = id.all())
        except:
            return False
     # returning data from database by user id address
    @staticmethod
    def get_all_vehicle_by_userid_address(address):
        try:
            return AddVehicles.objects.filter(user = address)
        except:
            return False
    
   


    def __str__(self):
	    return self.user.fullname + "  |   " + self.user.email + " |   " + self.model + " |   " 

    



    

