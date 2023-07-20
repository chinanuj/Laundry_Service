from django.shortcuts import render
from django.contrib.auth import get_user_model
from clothselection.models import cloth_selection
import datetime

User = get_user_model()

def upi(request):
    return render(request,"UPI.html")

def index1(request):
    entry1 = User.objects.first()
    max_last_login = entry1.last_login
    entry_all = User.objects.all()
    max_last_login = None 
    for obj in entry_all:
        if obj.last_login is not None and (max_last_login is None or max_last_login < obj.last_login):
            max_last_login = obj.last_login
    entry = User.objects.filter(last_login = max_last_login)
    items = cloth_selection.objects.filter(name__in=[user.username for user in entry])
    context = {'items': items, 'entry': entry}
    return render(request, "index1.html", context)


def clothselection(request):
    if request.method == 'POST':
        entry1 = User.objects.first()
        max_last_login = entry1.last_login
        entry_all = User.objects.all()
        max_last_login = None 
        for obj in entry_all:
            if obj.last_login is not None and (max_last_login is None or max_last_login < obj.last_login):
                max_last_login = obj.last_login
        entry = User.objects.filter(last_login=max_last_login)
        inputs = cloth_selection()
        inputs.time = datetime.datetime.now().strftime('%H:%M:%S   %d/%m/%Y')
        inputs.name = entry.first().username
        inputs.shirt = request.POST.get('shirt')
        inputs.Pants = request.POST.get('pants')
        inputs.Jeans = request.POST.get('jeans')
        inputs.Towel = request.POST.get('towel')
        inputs.shirt_image = request.FILES.get('uplshirt')
        inputs.Pants_image = request.FILES.get('uplpant')
        inputs.Jeans_image = request.FILES.get('upljeans')
        inputs.Towel_image = request.FILES.get('upltowel')
        inputs.save()

    return render(request, "clothselection.html")
