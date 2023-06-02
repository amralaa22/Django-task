from django.contrib import admin
from django.urls import path
from myaccount.views import *
urlpatterns=[
    path("",login, name="login"),
    path("Register/",register,name="register"),
    path("Logout/",logout, name="logout"),
]