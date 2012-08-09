from django.http import HttpResponse

#from django.template import Context, loader
from django.shortcuts import render_to_response
from django.utils import simplejson

def home(request):
    return render_to_response('home.html')

def auth(request):
    pass

#serialize object to json
def json_test(request):
    test_dict = {'a': 1, 'b': 2, 'c': 3}
    return HttpResponse(simplejson.dumps(test_dict), 
                              mimetype='application/json')

