from distutils.log import error
from email import message
from django.contrib.auth.hashers import make_password 
from django.shortcuts import redirect, render
from UserManagementSystem.models.registerModel import CustomUser
from django.views import View
from django.contrib import messages


class EditProfile(View):
    def get(self, request):
        email=request.session.get('user')
        user=CustomUser.get_user_by_email(email)
        userDict={'user':user}
        if user.user_type != "Vendor": 
            return render(request , 'user/edit_profile.html',userDict)
        else:
            return render(request , 'dashboard/users-profile.html',userDict)

    def post(self, request):
        postData = request.POST
        fullname =postData.get('full_name')
        phone =postData.get('phone')
        email =postData.get('email')
        profile=request.FILES.get('profile_pic')
        password  =postData.get('password')

         
        
        user=CustomUser.get_user_by_email(email)
        error_msg=None

        # a list comprehension to convert int to list
        phonee=[int(x) for x in str(phone)]
        #checking validation from backend
        if (not fullname):
            error_msg="please enter your fullname"
        elif (not phone):
            error_msg="please enter your phone"
        elif (len(phonee) != 10):
            error_msg="please enter your correct phone no"


        if not error_msg:
            try:
                # updating data
                user.fullname=fullname
                user.phone=phone         
                if profile != None and profile != " " :
                    user.profile_pic=profile          
                if password:
                    if len(password)<7:
                        error_msg="password must be more than 7 digits long"
                    else:
                        user.password=make_password(password)

                if not error_msg:
                    #data updated
                    user.update_profile()
                    messages.success(request,'your profile updated successfully')
                    return redirect('editProfile')
                else:
                    messages.error(request,error_msg)

            except:
                messages.error(request,'failed to update your profile')
        else:
            messages.error(request,f"{error_msg}")
  
        return redirect('editProfile')

        
 