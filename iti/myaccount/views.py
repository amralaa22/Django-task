from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import *
from .form import RegistrationAdminform, RegistrationAdminformModel
from django.contrib.auth import login,authenticate
from .models import *
from django.views.decorators.http import require_http_methods
# Create your views here.
def userlist(request):
    context={}
    for u in Myuser.objects.all():
        print(u)
    context['users'] = Myuser.objects.all()
    return render(request,'listusers.html',context)


def Login(request):
    context={}
    if(request.method == 'POST'):
        u=Myuser.objects. filter(username = request.POST['logname'],email = request.POST['logemail'],password = request.POST['logpassword'])
        userobj=authenticate(username=request.POST['logname'],password =request.POST['logpassword'] )
        if(len(u)!= 0 and userobj is not None):
            #add username in session
            request.session['logname'] = u[0].username 
            login(request,userobj)
            return HttpResponseRedirect('/Course')
        else:
            context['msg']= 'invalid username, email , password'
    return render(request,'register.html',context=context)

def register(request):
    if (request.method == 'POST'):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        u = Myuser(username = username)
        u.password = password
        u.email = email
        u.save()

    return render(request,'register.html')

def logout(request):
    request.session.clear()
    return render(request,'register.html')

def RegistrationAdmin(request):
    f= RegistrationAdminform()
    context={}
    context['form']=f
    f=RegistrationAdminform(request.POST)
    if(request.method=='POST'):
        if(f.is_bound and f.is_valid()):
            User.objects.create_superuser(username=request.POST['username'],password=request.POST['password'])
            return HttpResponseRedirect('/admin')
    return render(request,'RegistrationAdmin.html',context)
    # return HttpResponse('RegistrationAdmin')
    
@require_http_methods(['POST','GET'])
def RegistrationAdminModel(request):
    f=RegistrationAdminformModel()
    context={}
    context['form']=f
    if(request.method=='POST'):
        f=RegistrationAdminformModel(request.POST)
        if(f.is_bound and f.is_valid()):
            f.save()
    return render(request,'RegistrationAdminModel.html',context)
