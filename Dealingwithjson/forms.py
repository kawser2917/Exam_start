from django import forms
from .models import jsonToSql

class Updatedata(forms.ModelForm):
    class Meta:
        model = jsonToSql
        fields ='__all__'
        widgets = {
            'date': forms.DateInput(attrs={'class':"col-sm-12"}),
            'trade_code': forms.TextInput(attrs={"class":'col-sm-12'}),
            'high':  forms.TextInput(attrs={"class":'col-sm-12'}),
            'low':   forms.TextInput(attrs={"class":'col-sm-12'}),
            'open':  forms.TextInput(attrs={"class":'col-sm-12'}),
            'close': forms.TextInput(attrs={"class":'col-sm-12'}),
            'volume':forms.TextInput(attrs={"class":'col-sm-12'}),
        }
       