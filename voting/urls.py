from django.urls import path

from . import views

app_name = 'voting'

urlpatterns = [
    path('leaderboard', views.leaderboard, name='leaderboard'),
]
