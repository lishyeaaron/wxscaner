# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import *
from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponseRedirect
import requests
import json

# Create your views here.

def DevIdInterface(request):
    info1 = info.objects.get(id=1) 
    devid = info1.devid
    return JsonResponse({'devid':devid})

def index(request):
    info1 = info.objects.get(id=1)
    devid =info1.devid
    context = {'devid':devid}
    return render(request,'qrcode/index.html',context)

def uploadinfo(request,devid):

    info1 = info.objects.get(id=1) 
    # info1=info()
    if info1.devid == "0":
        if devid =="99":
            pass
        elif devid=="0":
            pass
        else:
            info1.devid=devid
            info1.save()            
    else:
        if devid=="99":
            info1.devid="0"
            info1.save()
        elif devid =="0":
            pass
        else:
            pass
    return redirect('/qrcode/index')



def getimgsrc(request):
    response = requests.get('http://114.55.6.49:7888/imgserver/AccountManagerTaskInterface')
    result = response.text.encode('utf-8')
    jsonData = json.loads(result)
    if len(jsonData) == 0:
        return JsonResponse({'imgsrc':"/static/images/qrcode.jpg"})
    else:
        imgsrc = jsonData['image_url']
        return JsonResponse({'imgsrc':imgsrc})

def clearcache(request):
    while True:
        try:
            response = requests.get('http://114.55.6.49:7888/imgserver/AccountManagerTaskInterface')
            result = response.text.encode('utf-8')
            jsonData = json.loads(result)
            jsonData = json.loads(result)
            if len(jsonData) == 0:
                return JsonResponse({'imgsrc':"/static/images/qrcode.jpg"})
            else:
                continue    
        except:
            return JsonResponse({'imgsrc':"/static/images/qrcode.jpg"})

