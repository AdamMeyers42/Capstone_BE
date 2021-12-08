from django.urls import path
from . import views

urlpatterns = [
    path('injury/', views.FantasyFootball.as_view()),
]