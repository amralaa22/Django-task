from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
from trainee.models import *
# Create your views here.
def traineelist(request):
    if('logname' in request.session):
        trainees = Trainees.objects.all()
        context={}
        context['trainees']=trainees
        return render(request,'task/traineelist.html',context) #HttpResponse("Courselist")
    else:
        return HttpResponseRedirect('/')

def traineeadd(request):
    context ={}
    context['courses'] = Courses.objects.all()
    if('logname' in request.session):
        if(request.method == 'POST'):
            cat = Courses.objects.get(id = request.POST['course'])
            Trainees.objects.create(name = request.POST['coursename'],courseid= cat)
    return render(request,'task/traineeadd.html',context) #HttpResponse("Traineeadd")

def traineeupdate(request,ID):
    context={}
    context['courses'] = Courses.objects.all()
    context['trainee'] = Trainees.objects.get(id = ID)
    if('logname' in request.session):
        if(request.method == 'POST'):
            Trainees.objects.filter(id = ID).update(name = request.POST['traineename'],courseid = Courses.objects.get(id=request.POST['coursename']))
            return HttpResponseRedirect('/Trainee') #HttpResponse("Trainee "+str (id)+"updated")
        return render(request,'task/traineeupdate.html',context)
    else:
        return HttpResponseRedirect('/')

def traineedelete(request, ID):
    Trainees.objects.filter(id=ID).delete()
    return HttpResponseRedirect('/Trainee')#HttpResponse("Trainee "+str(ID)+"deleted")