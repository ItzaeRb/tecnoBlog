from django.http import HttpResponse
from django.template import loader

def homePage(request):
    return HttpResponse(f'Home')
