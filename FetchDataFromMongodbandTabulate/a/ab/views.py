from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json
from django.http import HttpResponse
from django.http import JsonResponse

from .models import sensor
import pymongo
import re
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


def cleanupjson(inpjson):
            devdata=inpjson.get('0')
            if devdata == '':
                return
            jsondat = json.loads(devdata)
            return jsondat
        

def showdata(request):
        client = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
        db = client["data"]
        col = db["sensor"]
        x = col.find()
        filehandle = open('/home/user/data.json','w')
        strdat =  []
        deviceids = []
        count = 0 
        for data in x:
            count = count + 1
            jsondat = cleanupjson(data)
            if not jsondat:
                    continue
            filehandle.write(json.dumps(jsondat))
            filehandle.write("")
            dataf={'id': data.get('_id') , 'slno':count , 'device':jsondat }          
            strdat.append(dataf)
        strdat.reverse()
        pages = Paginator(strdat,10)
        context = {'devdata':strdat,
                    'total': count }
        
        return(render(request,'devices.html',context=context))

        return HttpResponse(html)

def index(request):
        dev_list = cleanupjson(data)
        page = request.GET.get('page', 1)
        paginator = Paginator(dev_list, 10)
        try:
            devdata = paginator.page(page)
        except PageNotAnInteger:
            devdata = paginator.page(1)
        except EmptyPage:
            devdata = paginator.page(paginator.num_pages)
        context = {'devdata':strdat,
                    'total': count }
        return render(request, 'devices.html', { context=context })
