from django.shortcuts import  render
from django.contrib.auth.hashers import make_password 
from django.shortcuts import redirect
from UserManagementSystem.models.registerModel import CustomUser
from UserManagementSystem.models.add_location import Add_location
from django.views import View






class RegisterVendor(View):
    def get(self, request):
        location=Add_location.get_all_data()
        loc={
            "loc":location
        }
        return render(request , 'register_as_vendor.html',loc)

    def post(self, request):

        # saving user send data in variable
        postData = request.POST
        profile_picc=request.FILES.get('picture')

        district=Add_location.get_all_data()

        
        fullname =postData.get('fullname')
        username =postData.get('username')
        phone =postData.get('phone')
        email =postData.get('email')
        address=postData.get('address')
        usertype=postData.get('usertype')
        password  =postData.get('password')

        user_address = Add_location.get_address_by_name(address)
        district=Add_location.get_all_data()
        print(usertype)
        print(profile_picc)
        print("kushal")
        if usertype == "Renter":
             
            return render(request , 'register_as_customer.html' )
        
        else:
            license_pic=request.FILES.get('license_pic')
            print(license_pic)
            #status off for vendor
            status="Inactive"

            #Renter user object
            user = CustomUser(profile_pic = profile_picc, licence_pic = license_pic , fullname = fullname  , username = username , phone = phone , email = email , user_type = usertype , address = user_address , password = password ,status = status  )
            #saving user entered value in dictionary
            entered_value ={'profile_pic':profile_picc,'license_pic': license_pic,'fullname':fullname , 'username': username ,'phone':phone ,'email' :email, 'address':address}
            print("---------------")
            print(entered_value)

            #checking validation from backend
            error_msg= self.validateUser(user)
            # saving
            if (not error_msg):

                # to hash password
                user.password= make_password(user.password)
                print("password")
            
                #to save data in database
                user.register()
                msgg= 'Your account is created but to login you must be verified by admin so please wait for some time'
                return render(request , "login.html" , {'info':msgg})
            else:

                data = {'error':error_msg ,'values':entered_value ,"dic":district}    
                print("some kind of error")    
                return render(request , 'register_as_vendor.html' , data)

    #  checking validation
    def validateUser(self , user):
        error_msg= None

        # if (not user.fullname):
        #     error_msg="please enter your firstname"
        # elif (not user.username):
        #     error_msg="please enter your username"
        # elif user.isExists_username():
        #     error_msg="username already register"
        # elif (len(user.username) < 4):
        #     error_msg="username should be more than 4 digits long"
        # elif (not user.phone):
        #     error_msg="please enter your phone no"
        # elif (len(user.phone) != 10):
        #     error_msg="please enter your correct phone no"
        # elif (not user.email):
        #     error_msg="please enter your email"
        # elif user.isExists_email():
        #     error_msg="Email  already register"
        # elif (user.email[user.email.index('@') + 1:] != "gmail.com"):
        #     error_msg="Email domail should be gmail.com"
        # elif (not user.password):
        #     error_msg="please Enter password"
        # elif (len(user.password) < 7):
        #     error_msg="password must be more than 7 digits long"
        

        return error_msg

       