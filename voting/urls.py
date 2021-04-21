from django.urls import path

from . import views

app_name = 'voting'

urlpatterns = [
    path('vote', views.vote_screen, name='vote_screen'),
]
