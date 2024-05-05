from django.urls import path
from . import views

app_name = 'testdb'
urlpatterns = [
    path("", views.index, name="index"),
]
