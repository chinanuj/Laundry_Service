from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("clothselection.html",views.clothselection, name = "clothselection"),
    path("index1.html",views.index1, name = "index1"),
    path("UPI.html",views.upi,name = "UPI"),
]