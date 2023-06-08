from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

from .forms import *
from .models import *
from trainee.models import *
from django.views import View
from django.views.generic import ListView,CreateView
# Create your views here.

class Courseadding(CreateView):
    model= Courses
    template_name='course/courseadd.html'
    fields='__all__'

    def form_valid(self,form):
        return HttpResponseRedirect('/Course')

class Addcourse(View):
    def get(self,request):
        context={}
        context['form'] = Courseform()
        return render(request,'task/courseadd.html',context)
    
    def post(self,request):
        f=Courseform(request.POST)
        if(f.is_bound and f.is_valid()):
            f.save()

        return HttpResponse('<h1>POST method</h1>')

class Listcourse(ListView):
    model= Courses
    template_name = 'course/course_list.html'




# def courselist(request):
#     return render(request,'task/courselist.html') #HttpResponse("Courselist")
       

# def courseadd(request):
#     return render(request,'task/courseadd.html') #HttpResponse("Courseadded")

# def courseupdate(request,id):
#     return HttpResponseRedirect('/Course') #HttpResponse("Course "+str (id)+" updated")

# def courseDelete(request,ID):
#     return HttpResponseRedirect('/Course') #HttpResponse("Course "+str (ID)+" updated")
