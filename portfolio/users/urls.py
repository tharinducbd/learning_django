from django.urls import include, path, re_path

from users.views import dashboard


app_name = "users"
urlpatterns = [
    re_path(r"^accounts/", include("django.contrib.auth.urls")),
    re_path(r"^dashboard/", dashboard, name="dashboard"),
]