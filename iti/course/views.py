from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
from trainee.models import *
# Create your views here.
def courselist(request):
    return render(request,'task/courselist.html') #HttpResponse("Courselist")
       

def courseadd(request):
    return render(request,'task/courseadd.html') #HttpResponse("Courseadded")

def courseupdate(request,id):
    return HttpResponseRedirect('/Course') #HttpResponse("Course "+str (id)+" updated")

def courseDelete(request,ID):
    return HttpResponseRedirect('/Course') #HttpResponse("Course "+str (ID)+" updated")
