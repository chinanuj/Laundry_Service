
# def filepath(request, filename):
#     old_filename = filename
#     timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
#     filename = "%s%s" % (timeNow,old_filename)
#     return os.path.join("data/media/",filename)   
from django.db import models
from django.db.models import Model
import os
import datetime

class cloth_selection(models.Model):
    time =  models.CharField(max_length=100)
    name = models.CharField(default="",max_length=100)
    shirt = models.IntegerField(default="")
    Pants = models.IntegerField(default="")
    Jeans = models.IntegerField(default="")
    Towel = models.IntegerField(default="")    
    shirt_image = models.ImageField(upload_to="data/media",default="")
    Pants_image = models.ImageField(upload_to="data/media",default="")
    Jeans_image = models.ImageField(upload_to="data/media",default="")
    Towel_image = models.ImageField(upload_to="data/media",default="")
    