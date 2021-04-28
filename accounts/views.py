from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User 
from django.contrib import messages,auth
from django.contrib.auth.decorators import login_required
from hiretubers.models import Hiretuber
from templated_email import send_templated_mail

# Create your views here.



def login(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        password = request.POST['password']
        user = auth.authenticate(username = uname,password = password)

        if user is not None:
            auth.login(request, user)
            messages.info(request, 'You are logged in')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Invalid credentials')
            return redirect('login')
    if request.user.is_authenticated:
        return render(request,'accounts/dashboard.html')
    return render(request, 'accounts/login.html')

def register(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        fullname = fname +" "+ lname
        uname = request.POST['uname']
        email = request.POST['email']
        email_list = [email]
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(username = uname).exists():
                messages.warning(request, 'Username already exists')
                return redirect('register')
            if User.objects.filter(email = email).exists():
                messages.warning(request, 'Email already exists')
                return redirect('register')
            if len(password) < 7:
                messages.warning(request,'Password should be atleast 7 characters long')
                return redirect('register')
        else:
            messages.warning(request, 'Password does not match')
            return redirect('register')
        
        send_templated_mail(
        template_name = 'newuser', 
        from_email = 'siddhantutube4@gmail.com',
        recipient_list = email_list,
        context = {

            'full_name':fullname,
            'username' : uname,
    
        }
    )
        user = User.objects.create_user(first_name = fname,last_name = lname,username  = uname,email = email,password = password)
        user.save()

        messages.success(request,'Account created succesfully')
        return redirect('login')
    if request.user.is_authenticated:
        return render(request,'accounts/dashboard.html') 
    return render(request,'accounts/register.html')

def logout_user(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def dashboard(request):
    user_id = request.user.id
    youtubers = Hiretuber.objects.filter(user_id = user_id)
    data = {
        'youtubers' : youtubers,
    }
    return render(request,'accounts/dashboard.html',data)
