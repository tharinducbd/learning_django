from django.http import HttpResponse
from django.shortcuts import render

from .models import House, Student, Subject, Teacher


def index(request):
    houses = House.objects.all()
    teachers = Teacher.objects.all()
    subjects = Subject.objects.all()
    students = Student.objects.all()

    context = {
        "all_houses": houses,
        "all_teachers": teachers,
        "all_subjects": subjects,
        "all_students": students,
    }

    return render(request, "administration/index.html", context)


def models(request, model_name):
    if model_name == 'houses':
        houses = House.objects.all()
        context = {"all_houses": houses}
    elif model_name == 'teachers':
        teachers = Teacher.objects.all()
        context = {"all_teachers": teachers}
    elif model_name == 'subjects':
        subjects = Subject.objects.all()
        context = {"all_subjects": subjects}
    elif model_name == 'students':
        students = Student.objects.all()
        context = {"all_students": students}

    return render(request, "administration/models.html", context)
