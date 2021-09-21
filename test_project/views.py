from django.shortcuts import render
from django.http import HttpResponse ,JsonResponse
from django.contrib.auth.models import User
def index(request):
    return render(request,'main.html')


def login(request):
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
