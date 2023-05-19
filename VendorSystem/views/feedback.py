from django.shortcuts import redirect, render
from django.views import View
from VendorSystem.models.vendor_feedback import VendorFeedback
from UserManagementSystem.models.registerModel import CustomUser




# Create your views here.


     
class Feedback(View):
    def get(self,request):
        #extracting user object by id
        id=request.session.get('id')
        user = CustomUser.get_user_by_id(id)

        feedback_history = VendorFeedback.get_all_feedback_by_userid(user)

        dict={
            'feedback':feedback_history
        }
        return render(request , 'dashboard/feedback.html',dict)


    def post(self,request):
        # saving user send data in variable
        postData = request.POST
        vendor_msg =postData.get('vendor_msg')

        #extracting user object by id
        id=request.session.get('id')
        user = CustomUser.get_user_by_id(id)

    

        feedback= VendorFeedback(
            vendor_id=user,
            feedback=vendor_msg,
            feedback_reply="",

        )
        feedback.feedback_save()

        return redirect('feedback')

    







    