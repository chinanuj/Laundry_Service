from django.shortcuts import render
from django.contrib.auth import get_user_model
from clothselection2.models import cloth_selection_1
import datetime

User = get_user_model()

def upi2(request):
    entry1 = User.objects.first()
    max_last_login = entry1.last_login
    entry_all = User.objects.all()
    max_last_login = None 
    for obj in entry_all:
        if obj.last_login is not None and (max_last_login is None or max_last_login < obj.last_login):
            max_last_login = obj.last_login
    entry = User.objects.filter(last_login = max_last_login)
    items = cloth_selection_1.objects.filter(name__in=[user.username for user in entry]).last()
    total1 = items.Total * 80
    return render(request, "UPI2.html",{"total1":total1})


def index1(request):
    entry1 = User.objects.first()
    max_last_login = entry1.last_login
    entry_all = User.objects.all()
    max_last_login = None 
    for obj in entry_all:
        if obj.last_login is not None and (max_last_login is None or max_last_login < obj.last_login):
            max_last_login = obj.last_login
    entry = User.objects.filter(last_login = max_last_login)
    items = cloth_selection_1.objects.filter(name__in=[user.username for user in entry])
    context = {'items': items, 'entry': entry}
    return render(request, "index2.html", context)


def cost(request):
    if request.method == 'POST':
        entry1 = User.objects.first()
        max_last_login = entry1.last_login
        entry_all = User.objects.all()
        max_last_login = None 
        for obj in entry_all:
            if obj.last_login is not None and (max_last_login is None or max_last_login < obj.last_login):
                max_last_login = obj.last_login
        entry = User.objects.filter(last_login=max_last_login)
        inputs = cloth_selection_1()
        inputs.time = datetime.datetime.now().strftime('%H:%M:%S   %d/%m/%Y')
        inputs.name = entry.first().username
        inputs.Jacket = request.POST.get('Jacket')
        inputs.Blazer = request.POST.get('Blazer')
        inputs.Hoodie = request.POST.get('Hoodie')
        inputs.Blanket = request.POST.get('Blanket')
        inputs.jacket_image = request.FILES.get('upljacket')
        inputs.blazer_image = request.FILES.get('uplblazer')
        inputs.hoodie_image = request.FILES.get('uplhoodie1')
        inputs.blanket_image = request.FILES.get('uplblanket1')
        inputs.Total = int(request.POST.get('Jacket')) + int(request.POST.get('Blazer')) + int(request.POST.get('Hoodie')) + int(request.POST.get('Blanket'))
        inputs.save()
        

    return render(request, "cost.html")