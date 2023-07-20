from django.shortcuts import render
from django.contrib.auth.models import User, auth
from laundry_app.models import ABOUTus
from clothselection.models import cloth_selection
from django.contrib.auth import get_user_model
from clothselection.models import cloth_selection


User = get_user_model()

def welcome(request):
    entry1 = User.objects.first()
    max_last_login = entry1.last_login
    entry_all = User.objects.all()
    max_last_login = None 
    for obj in entry_all:
        if obj.last_login is not None and (max_last_login is None or max_last_login < obj.last_login):
            max_last_login = obj.last_login

            
    entry = User.objects.filter(last_login = max_last_login).last()
    name = entry.username
    return render(request,"welcome.html",{'name':name})

def signup(request):
    return render(request,"signup.html")
def services(request):
    return render(request,"services.html")
def price(request):
    return render(request,"price.html")
def login2(request):
    return render(request,"login2.html")

def contactus(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        input1 = ABOUTus(name = name, email = email, message = message)
        input1.save()
        
    return render(request,"contactus.html")

def aboutus(request):
    return render(request,"aboutus.html")
# def clothselection(request):
#     return render(request, "clothselection.html")