from django.shortcuts import render,redirect
from .models import ContactUs
from django.contrib import messages
# Create your views here.

    
def submit_form(request):
    fname = request.POST['fname']
    phone = request.POST['phone']
    email = request.POST['email']
    company_name = request.POST['cname']
    subject = request.POST['subject']
    detailed_message = request.POST['message']
    contact = ContactUs(full_name=fname,phone=phone,email=email,company_name=company_name,subject=subject,detailed_message=detailed_message)
    contact.save()
    messages.success(request,'Succesfully Submitted')
    return redirect('contact')