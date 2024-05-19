from django import forms
from django.db.models.base import Model

from .models import House, Student, Subject, Teacher


class HouseModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj: Model) -> str:
        return f"{obj.name} ({obj.emblem})"


class SubjectMultipleModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj: Model) -> str:
        return f"{obj.name} {obj.id}"


class AddStudentForm(forms.Form):
    name = forms.CharField(label="Full Name",)
    house = HouseModelChoiceField(queryset=House.objects.all(),
                                   empty_label="Select the House",
                                   widget=forms.RadioSelect,
                                   )
    subjects = SubjectMultipleModelChoiceField(queryset=Subject.objects.all(),
                                               widget=forms.RadioSelect,
                                               )
