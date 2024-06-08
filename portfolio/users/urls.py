from django.urls import include, path, re_path

from users.views import dashboard

from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy


app_name = "users"
urlpatterns = [
    re_path(r"^accounts/", include("django.contrib.auth.urls")),
    path("password_change",
         auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('users:password_change_done')),
         name="password_change"),
    re_path(r"^dashboard/", dashboard, name="dashboard"),
]
