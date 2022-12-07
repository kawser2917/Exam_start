from django.shortcuts import render,HttpResponseRedirect
from .models import jsonToSql
import json
from .forms import Updatedata


def home(request):
    f = open('data/stock_market_data.json')
    json_data = json.load(f)
    return render(request,'Dealingwithjson/home.html',{"data":json_data})

def crud(request):
    f = open('data/stock_market_data.json')
    json_data = json.load(f)
    # print(json_data)
    # jsonToSql.objects.all().delete()
    # ---------------------------------    This is taking lot of time needs to improve ------------------->
    # for i in json_data:
    #     jsonToSql.objects.create(date=i['date'],trade_code=i['trade_code'],high=i['high'],low=i['low'],open=i['open'],close=i['close'],volume=i['volume'])
    data = jsonToSql.objects.all().order_by("trade_code")
    return render(request,'Dealingwithjson/crud.html',{'data':data})

def update_data(request,id):
    if request.method == "POST":
        pi = jsonToSql.objects.get(pk=id)
        fm =  Updatedata(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/updatedata/')
    else:
        pi = jsonToSql.objects.get(pk=id)
        fm = Updatedata(instance=pi)
    return render(request,"Dealingwithjson/updatedata.html",{"form":fm})

def delete_data(request,id):
    if request.method == "POST":
        pi = jsonToSql.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/updatedata/')
