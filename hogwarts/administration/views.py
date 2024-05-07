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
