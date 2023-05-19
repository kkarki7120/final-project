from asyncio.windows_events import NULL
from django.db import models
from UserManagementSystem.models.add_location import Add_location


# # Create your models here.

# user models
class CustomUser(models.Model):
    Status = (('Active','Active'),('Inactive','Inactive'))
    User = (('Renter','Renter'),('Vendor','Vendor'))

    id = models.AutoField(primary_key=True,  unique=True)
    fullname = models.CharField(max_length=100, null=True)
    username= models.CharField(max_length=50,unique=True) 
    phone = models.IntegerField()
    email = models.EmailField()
    user_type= models.CharField(choices=User, max_length=25, default='Renter')
    address= models.ForeignKey(Add_location, on_delete=models.CASCADE) 
    profile_pic=models.ImageField(upload_to='media/profile_pic',default='media/profile_pic/default.jpg')
    licence_pic=models.ImageField(upload_to='media/licence_pic',default=NULL)
    password = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now=True)
    status= models.CharField(choices= Status, max_length=25, default='Active')
    

    # To save in model in database
    def register(self):
        self.save()
    # To update in model in database
    def update_profile(self):
        self.save()
    
    #check whether user with same email exist or not in database
    def isExists_email(self):
        if CustomUser.objects.filter(email = self.email):
            return True
        return False

    
    #check whether user with same username exist or not in database
    def isExists_username(self):
        if CustomUser.objects.filter(username = self.username):
            return True
        return False

    #returning data from database
    @staticmethod
    def get_user_by_email(email):
        try:
            return CustomUser.objects.get(email = email)
        except:
            return False

    #returning data from database
    @staticmethod
    def get_user_by_address(address):
        try:
            return CustomUser.objects.filter(address = address , user_type = "Vendor")
        except:
            return False

    #returning data from database
    @staticmethod
    def get_user_by_id(id):
        try:
            return CustomUser.objects.get(id = id)
        except:
            return False

    @staticmethod
    def get_user_by_in_inlist(id):
        try:
            return CustomUser.objects.get(id = id)
        except:
            return False

    def __str__(self):
	    return self.username

    



    

