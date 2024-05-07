from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_list_or_404 ,render
from django.urls import reverse
from django.views import generic

from .models import Teacher


class TeacherList(generic.ListView):
    template_name = "testdb/index.html"
    context_object_name = "list_of_teachers"

    def get_queryset(self) -> QuerySet[Any]:
        """Return the list of teachers"""
        return Teacher.objects.all().order_by("-age")
