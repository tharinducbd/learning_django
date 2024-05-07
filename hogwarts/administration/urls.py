from django.urls import path
from . import views


app_name = "administration"
urlpatterns = [
    path("", views.index, name="index"),
    path("models/<str:model_name>", views.models, name="models"),
]
