from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

# @login_required(login_url='login')
def home(request):
    return render(request,'home.html')
    # return redirect("home") 

def BioHome(request):
    return render(request,'BioHome.html')


def LoginPage(request):
    if request.method=="POST":
        username = request.POST.get('username')
        pass1 = request.POST.get('password')

        check_user= authenticate(request,username=username,password=pass1)
        if check_user is not None:
            return redirect("home")
        else:
            return HttpResponse("Username or Password is incorrect!")
 
    return render(request,'login.html')

def SignupPage(request):
    if request.method=="POST":
        uname=request.POST.get("Username")
        email=request.POST.get("email")
        pass1=request.POST.get("password1")
        pass2=request.POST.get("password2")
    
        if pass1 != pass2:
            return HttpResponse("your password and confirm password is not same")
        else:
            my_user = User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')

    return render(request,'signup.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')