from django import forms
from .models import Geoinfo

class Size(forms.Form):
    ok = forms.CheckboxInput()

class SecondEndpointForms(forms.Form):
    zapytanie = forms.CharField(max_length=200)

