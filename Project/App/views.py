from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def graphical_method(request):
    return render(request, 'graphical_method.html')

def simplex_method(request):
    return render(request, 'simplex_method.html')
