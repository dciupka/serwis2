from django import forms

class Size(forms.Form):
    ok = forms.CheckboxInput()


class SecondEndpointForms(forms.Form):
    id = forms.IntegerField

