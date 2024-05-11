from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

def monthly_challanges(request,month):
    challanges = None
    if month == "january":
        challanges = "compleate Python"
    elif month == "febuary":
        challanges = "compleate Django"
    else:
        return HttpResponseNotFound("This month is not supported!!")
    return HttpResponse(challanges)
