from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views import generic

from .forms import TestForm
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


class HouseListView(generic.ListView):
    template_name = 'administration/list_houses.html'
    context_object_name = 'all_houses'

    def get_queryset(self) -> QuerySet[Any]:
        return House.objects.all()


class TeacherListView(generic.ListView):
    template_name = 'administration/list_teachers.html'
    context_object_name = 'all_teachers'

    def get_queryset(self) -> QuerySet[Any]:
        return Teacher.objects.all()


class SubjectListView(generic.ListView):
    template_name = 'administration/list_subjects.html'
    context_object_name = 'all_subjects'

    def get_queryset(self) -> QuerySet[Any]:
        return Subject.objects.all()


class StudentListView(generic.ListView):
    template_name = 'administration/list_students.html'
    context_object_name = 'all_students'

    def get_queryset(self) -> QuerySet[Any]:
        return Student.objects.all()


class HouseDetailView(generic.DetailView):
    model = House
    template_name = 'administration/detail_house.html'


class StudentDetailView(generic.DetailView):
    model = Student
    template_name = 'administration/detail_student.html'


class SubjectDetailView(generic.DeleteView):
    model = Subject
    template_name = 'administration/detail_subject.html'


class TeacherDetailView(generic.DetailView):
    model = Teacher
    template_name = 'administration/detail_teacher.html'


def house_fbv(request, house_id):
    # house = House.objects.get(id=house_id)
    house = get_object_or_404(House, id=house_id)
    return render(request, "administration/fbv_house.html", {
        "house": house
    })


def student_fbv(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    student_house = student.house
    student_subjects = student.subjects.all()

    unique_teachers, teacher_not_available = [], []

    for subject in student.subjects.all():
        if len(subject.teacher_set.all()) == 0:
            teacher_not_available.append(subject)
            continue
        else:
            for teacher in subject.teacher_set.all():
                if not teacher in unique_teachers:
                    unique_teachers.append(teacher)

    context = {
        'student': student,
        'student_house': student_house,
        'student_subjects': student_subjects,
        'unique_teachers': unique_teachers,
        'teacher_not_available': teacher_not_available,
    }

    return render(request, 'administration/fbv_student.html', context)


def form_test(request):
    context = {
        "test_form": TestForm(),
    }
    return render(request, "administration/0_test_form.html", context)
