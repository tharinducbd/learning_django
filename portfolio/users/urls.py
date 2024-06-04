from django.urls import path, re_path

from users.views import dashboard


app_name = "users"
urlpatterns = [
    re_path(r"^dashboard/", dashboard, name="dashboard"),
]
