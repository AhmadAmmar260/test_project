
from django import contrib
from django.shortcuts import redirect, render
from django.http import HttpResponse ,JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User

def index(request):
    return render(request,'main.html')

def home(request):
    return render(request,'index.html')
def login1(request):
    if request.method == 'POST':
        email = request.POST.get('emailll')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            
        return redirect('/home')
    else:
        return render(request,"login.html")


from django.views.decorators.csrf import csrf_exempt

def index(request):
    return render(request,'main.html')


def login3(request):
    return render(request,"login.html")
def testing_data(request):
    return render(request,"load_data.html")
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect

@csrf_exempt
def adding(request):
    
    #user = User.objects.create_user('john','ok223@gmail.com','jwwjeofji')
    #user.last_name='ii'
    #user.save()
    data={
        "name":"mohammed"
    }
    
    return JsonResponse(data)

def register(request):
    if request.method == "POST":
        username  = request.POST.get('username')
        email = request.POST['email']
        password  = request.POST['password']
        print(username,email,password)
        user = User.objects.create_user(username,email,password)
        user.last_name = 'me'
        user.save()
        request.session['username']=email
        return redirect('/login1')
    else:
        return render(request,'Register.html')

def Registeration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
            return redirect('home')
        else:
            return redirect('Registration',{'error':'this password or user is used'})
        

    else:
        form = UserCreationForm()
        context = {'form':form}
        return render(request,'registration/register.html',context)

def validate_username(request):
    username = request.GET.get('username')
    is_taken = User.objects.filter(username__iexact=username).exists()
    data = {'is_taken':is_taken}
    return JsonResponse(data)
       
    
       
    

import json
@csrf_protect

def get_data(request):
    a=request.GET['number']
    data={}
    print(a)
    i=int(a)*10
    numbe=1
    while i<((int(a)*10)+10):
    
        z={"cat{}".format(numbe):'http://127.0.0.1:8000/static/Cat/{}.jpg'.format(i)}
        numbe+=1
        i+=1
        data.update(z)
    #print(data)
    print(data)
    print(numbe)
    return JsonResponse((data))

def decode(session_id):
    session = Session.objects.get(session_key=session_id)
    uid = session.get_decoded().get('_auth_user_id')
    user = User.objects.get(pk=uid)
    return user


def post_data(request):
    b=request.POST
    session_key=request.session.session_key
    
    
    
    user=decode(session_key)
    print (user.username, user.password, user.email)
  
    a=request.POST['number']
    data={}
    print(a)
    i=int(a)*10
    numbe=1
    while i<((int(a)*10)+10):
        
  

        
        z={"cat{}".format(numbe):'http://127.0.0.1:8000/static/Cat/{}.jpg'.format(i)}
        numbe+=1
        i+=1
        data.update(z)
    #print(data)
    print(data)
    print(numbe)
    return JsonResponse((data))

