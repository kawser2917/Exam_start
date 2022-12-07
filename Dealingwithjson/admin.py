from django.contrib import admin
from .models import jsonToSql

# Register your models here.
@admin.register(jsonToSql)
class jsonToSqlAdmin(admin.ModelAdmin):
    list_display =['id','date','trade_code','high','low','open','close','volume']
