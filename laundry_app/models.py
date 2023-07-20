from django.db import models
from django.db.models import Model
import os
import datetime



class ABOUTus(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    
