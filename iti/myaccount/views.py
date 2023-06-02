from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
# Create your views here.
def userlist(request):
    context={}
    for u in Myuser.objects.all():
        print(u)
    context['users'] = Myuser.objects.all()
    return render(request,'listusers.html',context)


def login(request):
    context={}
    if(request.method == 'POST'):
        u=Myuser.objects. filter(username = request.POST['logname'],email = request.POST['logemail'],password = request.POST['logpassword'])
        if(len(u)!= 0):
            #add username in session
            request.session['logname'] = u[0].username 
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
