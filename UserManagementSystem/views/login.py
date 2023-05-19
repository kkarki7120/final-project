from django.contrib.auth.hashers import  check_password ,make_password
from django.shortcuts import redirect, render ,HttpResponseRedirect
from UserManagementSystem.models.registerModel import CustomUser
from django.views import View

#login backend is done in this class
class Login(View):
    return_url=None
    def get(self, request):
        if Login.return_url:
            Login.return_url = request.Get.get('return_url')
            return render(request , 'login.html')
        return render(request , 'login.html')
    
    def post(self, request):
        # saving user send data in variable
        postData = request.POST
        email =postData.get('email')
        password  =postData.get('password')

        #user object
        user = CustomUser.get_user_by_email(email) 
        entered_value ={'email':email}
        error_msg= None

        # validation   
        if (not email):
            error_msg="please enter your email"
        elif (not password):
            error_msg="please Enter password"
        
        # checking user
        if not error_msg: 

            #checking if user exist or not:
             
            if user:
                #checking user password:
                check=check_password(password , user.password)
                print(check)
                if check | (password == user.password):
                    #checking user status is active or not:
                    if user.status == "Active":
                        if Login.return_url:
                            print(Login.return_url)
                            return HttpResponseRedirect(Login.return_url)
                        else:
                            Login.return_url=None
                            request.session['user']=user.email
                            request.session['username']=user.username
                            request.session['id']=user.id
                            request.session['fullname']=user.fullname          
                            request.session['user_type']=user.user_type
                            return redirect('userIndex')
                    else:
                        error_msg="Your account is currently inactive please wait for some time or contact us using contact us page"
                else:
                    error_msg="password is incorrect"
            else:
                error_msg="Email isnot registered"
            data = {'error':error_msg ,'values':entered_value} 
            return render(request , 'login.html' , data)
            

            
        else:
            
            data = {'error':error_msg ,'values':entered_value} 
            return render(request , 'login.html' , data)



#logout function
def logout(request):
    request.session.clear()
    return redirect('login')