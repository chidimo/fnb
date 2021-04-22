from people.forms import LoginForm
from django.urls import reverse_lazy, path
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView

from . import views

app_name = "accounts"

urlpatterns = [
    path("login/", LoginView.as_view(form_class=LoginForm), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("leaderboard", views.leaderboard, name="leaderboard"),
    path("users", views.all_persons, name="all_persons"),
    path("profile/<int:pk>/", views.person_profile, name="profile"),
    path(
        "password_change/",
        PasswordChangeView.as_view(success_url=reverse_lazy("accounts:login")),
        name="password_change",
    ),
]
