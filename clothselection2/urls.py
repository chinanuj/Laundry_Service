from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("cost.html",views.cost, name = "cost"),
    path("index2.html",views.index1, name = "index1"),
    path("UPI2.html",views.upi2, name = "UPI2"),
]