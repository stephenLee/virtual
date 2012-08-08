from django.http import HttpResponse

#from django.template import Context, loader
from django.shortcuts import render_to_response

def home(request):
    return render_to_response('home.html')

def auth(request):
    pass
