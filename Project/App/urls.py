from django.urls import path
from . import views

urlpatterns = [
    # Home page
    path('', views.home, name='home'),

    # Graphical Method
    path('graphical/', views.graphical_method, name='graphical_method'),
    path('graphical/steps/', views.graphical_steps, name='graphical_steps'),
    path('graphical/solve/', views.graphical_solve, name='graphical_solve'),
    path('graphical/application/', views.graphical_application, name='graphical_application'),

    # Simplex Method
    path('simplex/', views.simplex_method, name='simplex_method'),
    path('simplex/steps/', views.simplex_steps, name='simplex_steps'),
    path('simplex/solve/', views.simplex_solve, name='simplex_solve'),  # Correctly mapped to simplex_solve view
    path('simplex/application/', views.simplex_application, name='simplex_application'),
    path('simplex/solver/', views.simplex_solver, name='simplex_solver'),  # For solving problems
]
