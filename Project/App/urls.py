from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('graphical-method/', views.graphical_method, name='graphical_method'),
    path('simplex-method/', views.simplex_method, name='simplex_method'),
]
