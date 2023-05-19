from django.db import models


# # Create your models here.

# user models
class Add_location(models.Model):
    id = models.AutoField(primary_key=True,  unique=True)
    location_name = models.CharField(unique=True, max_length=100)


    #Return all the district name
    def get_all_data():
        return Add_location.objects.all()

    @staticmethod
    def get_address_by_name(name):
        try:
            return Add_location.objects.get(location_name = name)
        except:
            return False


    def __str__(self):
	    return self.location_name