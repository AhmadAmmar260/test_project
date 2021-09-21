from django.shortcuts import redirect, render
from django.http import HttpResponse ,JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth

def index(request):
    return render(request,'main.html')

def home(request):
    return render(request,'index.html')
def login(request):
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
        return redirect('/login')
    else:
        return render(request,'Register.html')
       
    
       
    
