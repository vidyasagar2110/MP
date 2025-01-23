from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def graphical_method(request):
    return render(request, 'graphical_method.html')

def simplex_method(request):
    return render(request, 'simplex_method.html')

def graphical_steps(request):
    return render(request, 'graphical_steps.html')

def graphical_solve(request):
    return render(request, 'graphical_solve.html')

def graphical_application(request):
    return render(request, 'graphical_application.html')

def simplex_steps(request):
    return render(request, 'simplex_steps.html')

def simplex_solve(request):
    return render(request, 'simplex_solve.html')

def simplex_application(request):
    return render(request, 'simplex_application.html')
