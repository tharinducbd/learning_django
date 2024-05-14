from django import forms

from .models import House, Student, Subject, Teacher


class TestForm(forms.Form):
    name = forms.CharField(label="Full Name",)
    house = forms.ModelChoiceField(queryset=House.objects.all())
    subjects = forms.ModelMultipleChoiceField(queryset=Subject.objects.all())
