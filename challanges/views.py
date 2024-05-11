from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def january (request):
    return HttpResponse("Compleate Python")

def february(request):
    return HttpResponse("compleate django")
