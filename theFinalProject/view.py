from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def homePage(request):
    return render(request, "homePage.html")