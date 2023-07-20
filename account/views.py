from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages




def login(request):
    if request.method == 'POST' :
        username =request.POST.get('username')
        password = request.POST.get('password')
        user =auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,"")
            return redirect("http://127.0.0.1:8000/welcome.html")
        else:
            messages.success(request,"Invalid Credentials")
            return render(request, 'login.html', context={'hello': 'world'})
    else:
        return render(request, 'login.html', context={'hello': 'world'})


def register(request):
    if request.method == 'POST' :
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        #password2 = request.POST['password2']
        email = request.POST['email']
        user = User.objects.create_user(username=username, email=email, first_name=first_name,last_name=last_name,password= password1)
        user.save()
        print("user saved")
        return redirect("/account/login")
    else:
        return render(request, 'register.html', context={'hello': 'world'})

