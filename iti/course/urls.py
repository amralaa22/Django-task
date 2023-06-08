from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns=[
    path("",Listcourse.as_view(), name = "courselist"),
    path("Add/",Courseadding.as_view(), name = "courseadd"),
    path("Update/<int:id>",Listcourse.as_view(), name = "courseupdate"),
    path("Delete/<int:ID>",Listcourse.as_view(),name = "coursedelete"),
]