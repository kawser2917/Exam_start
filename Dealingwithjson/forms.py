from django import forms
from .models import jsonToSql

class Updatedata(forms.ModelForm):
    class Meta:
        model = jsonToSql
        fields ='__all__'