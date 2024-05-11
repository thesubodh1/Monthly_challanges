from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse

monthly_challange = {
    "january" : "learn Python",
    "february" : "learn Django",
    "march" : "learn react",
    "april" : "learn html",
    "may" : "learn css",
    'june' : "learn git",
    'july' : "jog for 20km",
    "august" : "loose 2 kg",
    "september" : "walk for 20 minutes",
    "october" : "break",
    "november" : "start a new job",
    "december" : "compleate if any pending"
}

# Create your views here. it also works
# def monthly_challange_dict(request,month):
#     if month in monthly_challanges:
#         return HttpResponse(monthly_challanges[month])
#     else:
#         return HttpResponseNotFound("this month doesnt exist")

def monthly_challange_number(request, month):
    months = list(monthly_challange.keys())
    try:
        redirect_month=months[month-1]
    except IndexError:
        return HttpResponseNotFound("invalid month")
    else: 
        redirect_path = reverse("month-challanges", args=[redirect_month])
        return HttpResponseRedirect(redirect_path)

def monthly_challanges(request,month):
    try:
        challanges = monthly_challange[month]
    except:
        return HttpResponseNotFound("This month is not supported!!")
    else:
        return HttpResponse(challanges)
    
