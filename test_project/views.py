from django.shortcuts import render
from django.http import HttpResponse ,JsonResponse
from django.contrib.auth.models import User
def index(request):
    return render(request,'main.html')


def login(request):
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

def post_data(request):
    a=request.POST
    print(a)
    return HttpResponse("hi")


