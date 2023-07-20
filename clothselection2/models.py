from django.db import models
from django.db.models import Model
import os
import datetime


class cloth_selection_1(models.Model):
    time = models.CharField(max_length=100)
    name = models.CharField(default="", max_length=100)
    Jacket = models.IntegerField(default="")
    Blazer = models.IntegerField(default="")
    Hoodie = models.IntegerField(default="")
    Blanket = models.IntegerField(default="")
    jacket_image = models.ImageField(upload_to="data/media", default="")
    blazer_image = models.ImageField(upload_to="data/media", default="")
    hoodie_image = models.ImageField(upload_to="data/media", default="")
    blanket_image = models.ImageField(upload_to="data/media", default="")
    Total = models.BigIntegerField(default=0)
