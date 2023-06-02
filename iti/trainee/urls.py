from django.contrib import admin
from django.urls import path
from trainee.views import * 

urlpatterns=[
    path('',traineelist,name='traineelist'),
    path('Add',traineeadd,name='traineeadd'),
    path('Update/<int:ID>',traineeupdate,name='traineeupdate'),
    path('Delete/<int:ID>',traineedelete,name='traineedelete'),
]