from django.db import models
from UserManagementSystem.models.registerModel import CustomUser


# # Create your models here.

# AddVehicles models
class VendorFeedback(models.Model):
    id = models.AutoField(primary_key=True,  unique=True)
    vendor_id=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    feedback = models.TextField()
    feedback_reply = models.TextField(null=True)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now=True )

    def feedback_save(self):
        self.save()
    
    # returning data from database by vendor id
    @staticmethod
    def get_all_feedback_by_userid(id):
        try:
            return VendorFeedback.objects.filter(vendor_id = id)
        except:
            return False


    def __str__(self):
	    return self.vendor_id.username + " " + self.vendor_id.email + " | " + self.feedback

    



    

