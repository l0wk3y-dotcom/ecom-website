from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib .auth import authenticate, login
from django.http import HttpResponseRedirect
from .models import Profile

def login_page(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        print(email,password)
        user_obj=User.objects.filter(username=email)
        if not user_obj.exists():
            messages.add_message(request,messages.ERROR,"Invalid credentials")
            print("1")
            return HttpResponseRedirect(request.path_info)
        user=authenticate(username=email,password=password)
        
        if not user:
            messages.add_message(request,messages.ERROR,"Invalid credentials")
            print("2")
            return HttpResponseRedirect(request.path_info)
        
        if not user_obj[0].profile.first().email_is_verified:
            messages.add_message(request,messages.ERROR,"Email is not verified")
            print("3")
            return HttpResponseRedirect(request.path_info)
        login(request,user)
        return redirect("/")
        
    return render(request,'accounts/login_page.html')



def register_page(request):
    if request.method=="POST":
        data=request.POST
        first_name=data.get('fname')
        last_name=data.get('lname')
        username=data.get('email')
        email=data.get('email')
        password1=data.get('password1')
        password2=data.get('password2')
        if not password1==password2:
            messages.add_message(request,messages.ERROR,'Passowrds do not match')
            return HttpResponseRedirect(request.path_info)
        
        if User.objects.filter(username=username).exists():
            messages.add_message(request,messages.ERROR,'email already exists')
            return HttpResponseRedirect(request.path_info)

        user=User(first_name=first_name,last_name=last_name,username=username,email=email)    
        user.set_password(password1)
        user.save()
        messages.add_message(request,messages.SUCCESS,'An email has been sent to you mail')
        
    return render(request,'accounts/register_page.html')


def activate_email(request,email_token):
    if email_token=="hello":
        return HttpResponse("hello")
    try:
        profile=Profile.objects.get(email_token=email_token)
        if profile:
            profile.email_is_verified= True
            profile.save()
            return HttpResponse("Your email has been verified")
        return HttpResponse("Something went wrong verify again!")
    except Exception as e:
        print(e)
        return HttpResponse("Something is wrong with the URL")
