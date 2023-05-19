
from django.shortcuts import redirect, render
from UserManagementSystem.models.contact_us import Contact_Us
from django.conf import settings
from django.core.mail import send_mail



# Create your views here.

from django.views import View

#login backend is done in this class
class Contact_US(View):
    def get(self, request):
        return render(request , 'index.html')
    
    def post(self, request):
        # saving user send data in variable
        postData = request.POST
        name =postData.get('name')
        email =postData.get('email')
        message =postData.get('message')

        print(name , email ,message)

        contact = Contact_Us(full_name=name, email=email,message=message)
        contact.contact_save()
        return redirect('index')

        # subject = f"Message from : {name} , Email = {email}"
        # message=message
        
        # email_from=settings.EMAIL_HOST_USER
        # try:
        #     send_mail(subject,message,email_from , ['kkarki761@gmail.com'])
        #     return redirect('index')
        # except:
        #     return redirect('contact')

     


    







    