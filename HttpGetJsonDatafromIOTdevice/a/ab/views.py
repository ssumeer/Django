from django.shortcuts import render

# Create your views here.
import json
from django.http import HttpResponse
from django.http import JsonResponse

from .models import sensor


import pprint

def homePageView(request):
        return HttpResponse('Hello, World!')


def send_json(request):

    data = []
    return JsonResponse(data, safe=False)


def savedata(request):
        print(request.body.decode('utf-8'))
        if 'application/json' in request.META['CONTENT_TYPE']:
            dat = json.loads(request.body.decode('utf-8'))
#            data.save()
            s = sensor(data=dat)
            s.save()
            return(HttpResponse("OK"))
        else:
            return(HttpResponse("NOT JSON"))
            
