from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Hiretuber
from youtubers.models import Youtuber
from django.core.mail import send_mail
from templated_email import send_templated_mail

# Create your views here.

    
    
    
    
    
def hiretuber(request,id):

    yt_email = Youtuber.objects.filter(id = id)
    yt_email_list = list(yt_email.values_list('email',flat=True))
    
    fname = request.POST['fname']
    lname = request.POST['lname']
    email = request.POST['email']
    tubername = request.POST['tubername']
    city = request.POST['city']
    state = request.POST['state']
    phonenumber = request.POST['phone']
    usermessage = request.POST['message']
    user_id = request.POST['user_id']
    
    send_templated_mail(
        template_name = 'welcome', 
        from_email = 'siddhantutube4@gmail.com',
        recipient_list = yt_email_list,
        context = {
            'message':usermessage,
            'full_name':request.user.get_full_name(),
            'city' : city,
            'email' : email,
            'tubername' : tubername,
        }
    )



    query = Hiretuber(first_name=fname,last_name=lname,tuber_id=id,email=email,tuber_name=tubername,city=city,phone = phonenumber,state=state,user_id=user_id,message=usermessage)
    query.save()
    messages.success(request,"Email sent Succesfully to {}".format(tubername))
    return redirect('youtubers')


