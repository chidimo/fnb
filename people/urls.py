from django.urls import reverse_lazy, path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'people'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('profile/<int:pk>/', views.personnel_detail, name='profile'),
]
