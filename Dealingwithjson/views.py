from django.shortcuts import render
import json

# Create your views here.
# f = open('fixtures/stock_market_data.json')
# json_data = json.load(f)

def home(request):
    f = open('data/stock_market_data.json')
    json_data = json.load(f)
    return render(request,'Dealingwithjson/home.html',{"data":json_data})
