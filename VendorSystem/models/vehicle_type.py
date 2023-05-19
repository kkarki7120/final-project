from django.db import models


# # Create your models here.

# AddVehicles models
class VehiclesTypes(models.Model):
    Status = (('Active','Active'),('Inactive','Inactive'))
    id = models.AutoField(primary_key=True,  unique=True)
    name = models.CharField(max_length=150)
    status= models.CharField(choices= Status, max_length=25, default='Active')

        #returning data from database
    @staticmethod
    def get_all_data():
        try:
            return VehiclesTypes.objects.all()
        except:
            return False
    
    #returning data from database
    @staticmethod
    def get_all_data_by_id(id):
        try:
            return VehiclesTypes.objects.get(id=id)
        except:
            return False
    

    def __str__(self):
	    return self.name

class Fuel_type(models.Model):
    Status = (('Active','Active'),('Inactive','Inactive'))
    id = models.AutoField(primary_key=True,  unique=True)
    name = models.CharField(max_length=150)
    status= models.CharField(choices= Status, max_length=25, default='Active')
    
    #returning data from database
    @staticmethod
    def get_all_data():
        try:
            return Fuel_type.objects.all()
        except:
            return False

    #returning data from database by id
    @staticmethod
    def get_all_data_by_id(id):
        try:
            return Fuel_type.objects.get(id=id)
        except:
            return False

    
    def __str__(self):
	    return self.name


class Company_name(models.Model):
    Status = (('Active','Active'),('Inactive','Inactive'))
    id = models.AutoField(primary_key=True,  unique=True)
    name = models.CharField(max_length=150)
    status= models.CharField(choices= Status, max_length=25, default='Active')
    
    #returning data from database
    @staticmethod
    def get_all_data():
        try:
            return Company_name.objects.all()
        except:
            return False

    #returning data from database by id
    @staticmethod
    def get_all_data_by_id(id):
        try:
            return Company_name.objects.get(id=id)
        except:
            return False

    
    def __str__(self):
	    return self.name

    

    
    



    

