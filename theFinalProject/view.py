from django.http import HttpResponse
from django.template import loader

def homePage(self, name):
    return HttpResponse(f'HomePage')
