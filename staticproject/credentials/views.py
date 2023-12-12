from django.contrib import messages, auth
from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    if request.method=="POST":
        uname=request.POST['uname']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword=request.POST['cpassword']
        from django.contrib.auth.models import User
        if password==cpassword:
            if User.objects.filter(username=uname).exists():
                messages.info(request,"username exists")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email exists")
                return redirect('register')
            else:
                user=User.objects.create_user(username=uname,first_name=fname,last_name=lname,email=email,password=password)
                user.save();
                return redirect('login')
        else:
            print("passwords did not matches")
            return redirect('register')
        return redirect('/')

    return render(request,"register.html")

def login(request):
    if request.method=='POST':
        username=request.POST['uname']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect("login")
    return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')
