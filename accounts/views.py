from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

def register(request):
    if request.method=='POST':
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        confirm_password=request.POST.get("confirm_password")

        if password != confirm_password:
            messages.error(request,'Password do not match')
            return redirect('register')
        
        if User.objects.filter(username=username).exists():
            messages.error(request,'Username already exists.')
            return redirect("register")

        if User.objects.filter(email=email).exists():
            messages.error(request,"Email already exists.")
            return redirect("register")

        user=User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        messages.success(
            request,'Account Created Succesfully Please Login'
        )

        return redirect("login")

    return render(request,"accounts/register.html")      

def login_view(request):
    if request.method == 'POST':
        username=request.POST.get("username")
        password=request.POST.get("password")

        user=authenticate(
            request,username=username,password=password
        )

        if user is not None:
            login(request,user)

            messages.success(request,'Login successful')

            return redirect('home')

        messages.error(request,'Invalid username or password')

    return render(request,"accounts/login.html")


def logout_view(request):

    logout(request)

    messages.success(request,"You have been logged out.")

    return redirect("home")






