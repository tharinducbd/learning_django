from django.urls import path
from . import views

app_name = 'testdb'
urlpatterns = [
    path("teachers/", views.TeacherList.as_view(), name="teacher_list"),
]
