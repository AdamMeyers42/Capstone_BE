from django.urls import path
from . import views

urlpatterns = [
    path('', views.InjuryReports.as_view()),
]