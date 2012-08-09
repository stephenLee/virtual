from django.http import HttpResponse

#from django.template import Context, loader
from django.shortcuts import render_to_response
from django.utils import simplejson

import json

def home(request):
    return render_to_response('home.html')

def auth(request):
    pass

#load local json file
def json_test(request):
    f = open('/home/lxd/virtual/visualization/weibo/data/hackr_event.json', 'r')
    content = f.read()
    f.close()
    data = simplejson.loads(content)
    return HttpResponse(simplejson.dumps(data), mimetype='application/json')

def visualization(request):
    return render_to_response('visual.html')
