from django import forms


class TestForm(forms.Form):
    name = forms.CharField(label="Full Name")
    house = forms.CharField(label="House")
