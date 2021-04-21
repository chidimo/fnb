from django.urls import reverse_lazy, path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'people'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('leaderboard', views.leaderboard, name='leaderboard'),
    path('users', views.all_persons, name='all_persons'),
    path('profile/<int:pk>/', views.person_profile, name='profile'),
    path('password_change/', auth_views.PasswordChangeView.as_view(
        success_url=reverse_lazy('people:login')), name='password_change'),
]
