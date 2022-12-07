from django.shortcuts import render
from .models import jsonToSql
import json


def home(request):
    f = open('data/stock_market_data.json')
    json_data = json.load(f)
    return render(request,'Dealingwithjson/home.html',{"data":json_data})

def crud(request):
    f = open('data/stock_market_data.json')
    json_data = json.load(f)
    # print(json_data)
    # jsonToSql.objects.all().delete()
    # for i in json_data:
    #     jsonToSql.objects.create(date=i['date'],trade_code=i['trade_code'],high=i['high'],low=i['low'],open=i['open'],close=i['close'],volume=i['volume'])
    data = jsonToSql.objects.all().order_by("id")
    return render(request,'Dealingwithjson/crud.html',{'data':data})
