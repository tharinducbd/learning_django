from django.urls import path
from . import views


app_name = "administration"
urlpatterns = [
    path("", views.index, name="index"),
    path("models/<str:model_name>", views.models, name="models"),
    path("houses/", views.HouseListView.as_view(), name="houses"),
    path("teachers/", views.TeacherListView.as_view(), name="teachers"),
    path("subjects/", views.SubjectListView.as_view(), name="subjects"),
    path("students/", views.StudentListView.as_view(), name="students"),
    path("houses/<int:pk>", views.HouseDetailView.as_view(), name="house_info"),
    path("students/<int:pk>", views.StudentDetailView.as_view(), name="student_info"),
    path("subjects/<int:pk>", views.SubjectDetailView.as_view(), name="subject_info"),
    path("teachers/<int:pk>", views.TeacherDetailView.as_view(), name="teacher_info"),
    path("fbv/house/<int:house_id>", views.house_fbv, name="fbv_house"),
    path("fbv/student/<int:student_id>", views.student_fbv, name="fbv_student"),
    path("students/add_student_html/", views.add_student_html, name="add_student_html"),
    path("students/add/", views.add_student, name="add_student"),
    path("fbv/student/<int:student_id>/update", views.update_student, name="update_student"),
]
