from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
# Create your views here.

def sample(request):
    return HttpResponse('hello world')
def sample1(request):
    return HttpResponse('welcome to django')
def sampleInfo(request):
    # data={"name":'raju','age':25,'city':'hyd'}
    data={"result":[1,2,3,4,5]}
    return JsonResponse(data)
def dynamicResponse(request):
    name=request.GET.get("name",'raju')
    city=request.GET.get("city",'hyderabad')
    return HttpResponse(f"hello {name} from {city}")
