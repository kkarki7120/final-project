import email
from email import message
from django.db import models


# # Create your models here.

# user models
class Contact_Us(models.Model):
    id = models.AutoField(primary_key=True,  unique=True)
    full_name = models.CharField(max_length=100)
    email=models.EmailField()
    message=models.TextField()
    date=models.DateTimeField(auto_now_add=True)

    def contact_save(self):
        self.save()

    def __str__(self):
	    return self.email

