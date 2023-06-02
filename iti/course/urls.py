from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns=[
    path("",courselist, name = "courselist"),
    path("Add/",courseadd, name = "courseadd"),
    path("Update/<int:id>",courseupdate, name = "courseupdate"),
    path("Delete/<int:ID>",courseDelete,name = "coursedelete"),
]