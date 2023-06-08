from django.contrib import admin
from django.urls import path
from myaccount.views import *
urlpatterns=[
    path("",Login, name="login"),
    path("Register/",register,name="register"),
    path("Logout/",logout, name="logout"),
    path('RegistrationAdmin',RegistrationAdmin,name='RegistrationAdmin'),
    path('RegistrationAdminModel',RegistrationAdminModel,name='RegistrationAdminModel'),
]